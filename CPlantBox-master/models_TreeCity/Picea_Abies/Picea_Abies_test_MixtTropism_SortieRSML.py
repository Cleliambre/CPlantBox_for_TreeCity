import plantbox as pb
import numpy as np

# --- 1. L'ENVIRONNEMENT PUR ---
class SolHumidite(pb.SoilLookUp):
    def __init__(self, cx=300, cy=0, cz=-80):
        super().__init__()

    def getDistance(self, pos):
        return np.sqrt((pos.x - self.cx)**2 + (pos.y - self.cy)**2 + (pos.z - self.cz)**2)
        
    def getValue(self, pos, organ=None):
        # Le sol ne connait que la position de l'eau
        distance = self.getDistance(pos)
        
        # Retourne uniquement une concentration/attractivité liée à l'eau
        return 1000 / (distance + 50)

#un sol plus complexe avec plusieurs poches d'eau  
class SolHumidite2(pb.SoilLookUp):
    def __init__(self, pics_humidite=None):
        super().__init__()
        # Si on ne donne pas de pics, on en crée une liste par défaut très dispersée
        if pics_humidite is None:
            self.pics = [
                (300, 0, -80),     # Poche originale (Droite, moyenne profondeur)
                (-250, 100, -120), # Poche (Gauche, profonde, décalée en Y)
                (100, -200, -40),  # Poche (Devant, très peu profonde)
                (-100, 150, -180)  # Poche (Derrière, très profonde)
            ]
        else:
            self.pics = pics_humidite
            
    def getDistance(self, pos):
        """Renvoie la distance minimale entre la position donnée et les pics d'humidité"""
        # Cherche la distance vers la flaque d'eau la plus proche
        distance_min = float('inf')
        for cx, cy, cz in self.pics:
            dist = np.sqrt((pos.x - cx)**2 + (pos.y - cy)**2 + (pos.z - cz)**2)
            if dist < distance_min:
                distance_min = dist
        return distance_min
        
    def getValue(self, pos, organ=None):
        #méthode "opportuniste" : on ne regarde que la poche d'eau la plus proche pour calculer l'humidité
        distance_min = self.getDistance(pos)
        return 1000 / (distance_min + 50)
    
        #méthode "cumulative" : on additionne l'humidité dégagée par toutes les poches d'eau, même les plus éloignées
        # Additionne l'humidité dégagée par toutes les poches
        #humidite_totale = 0
        #for cx, cy, cz in self.pics:
        #    dist = np.sqrt((pos.x - cx)**2 + (pos.y - cy)**2 + (pos.z - cz)**2)
        #    humidite_totale += 1000 / (dist + 50)
        #return humidite_totale

# --- 2. LE COMPORTEMENT PUR (Héritage de Tropism) ---
class MonTropismeMixte(pb.Tropism):
    def __init__(self, plant, n_trials, sigma, sol_humide, poids_grav=0.8, poids_eau=0.2):
        # 1. On initialise la classe mère C++ pb.Tropism
        super().__init__(plant, n_trials, sigma)
        
        #réutilisation des tropismes déjà existants
        self.t_gravite = pb.Gravitropism(plant, n_trials, sigma)
        self.t_eau = pb.Hydrotropism(plant, n_trials, sigma, sol_humide)

        # 2. On stocke nos paramètres spécifiques
        self.sol = sol_humide
        self.w_grav = poids_grav
        self.w_eau = poids_eau

    # On écrase (override) la méthode d'évaluation du tropisme
    def tropismObjective(self, pos, old, a, b, dx, organ=None):        
        # Calcul de l'objectif Gravité
        # 1. On demande au moteur C++ de calculer le score de gravité
        # Il va utiliser 'old', 'a' et 'b' pour évaluer la future trajectoire 
        # et renvoyer un score parfait entre 0 et 1.
        score_gravite = self.t_gravite.tropismObjective(pos, old, a, b, dx, organ)
        
        # Calcul de l'objectif Eau
        # 2. On fait exactement la même chose pour l'eau
        score_eau = self.t_eau.tropismObjective(pos, old, a, b, dx, organ)

        distance = self.sol.getDistance(pos)

        # 3. La Zone Neutre Anti-Noeuds :
        # Si la racine est dans un rayon de 40cm du centre de la poche d'eau,
        # on coupe l'attraction de l'eau pour qu'elle reprenne sa course droite.
        poids_eau_actuel = 0 if distance < 40 else self.w_eau
        
        # Retourne le score combiné
        return (score_gravite * self.w_grav) + (score_eau * poids_eau_actuel)

# --- 3. LE SCRIPT PRINCIPAL ---
plant = pb.RootSystem() #attention, RootSystem est deprecated mais c'est plus simple pour exporter en RSML
plant.readParameters("../../modelparameter_TreeCity/structural/Picea_Abies_hydro_v2.xml")

# On instancie notre sol et on l'assigne
#mon_sol = SolHumidite(cx=300, cy=0, cz=-80)
mon_sol2 = SolHumidite2()
plant.setSoil(mon_sol2)

# Initialisation
plant.initialize()

# On instancie notre tropisme mixte
tropisme_mixte = MonTropismeMixte(plant, 2.0, 1.5, mon_sol2, 0.26, 1)
tropisme_mixte2 = MonTropismeMixte(plant, 4.0, 0.5, mon_sol2, 0.01, 1)

plant.setTropism(tropisme_mixte, 3)

plant.setTropism(tropisme_mixte, 5)

plant.setTropism(tropisme_mixte,  2)

plant.setTropism(tropisme_mixte2, 7)

# Simulation
sim_time = 5000
dt = 50
n_steps = round(sim_time / dt)

for i in range(0, n_steps):
    plant.simulate(dt)
    plant.write("results/Picea_Abies_Mixte_" + str(i) + ".vtp")
plant.write("results/Picea_Abies_Mixte.rsml")

#export de la carte d'humidité pour ParaView
print("Génération du champ d'humidité 3D...")
x_min, x_max = -1000.0, 1000.0
y_min, y_max = -1000.0, 1000.0
z_min, z_max = -1000.0, 5.0
res = 50
xs = np.linspace(x_min, x_max, res)
ys = np.linspace(y_min, y_max, res)
zs = np.linspace(z_min, z_max, res)
with open("results/Picea_Abies_HumiditeSol_Mixte.vtk", "w") as f:
    # En-tête obligatoire pour ParaView
    f.write("# vtk DataFile Version 3.0\n")
    f.write("Champ d'humidite du sol - Tropisme Mixte\n")
    f.write("ASCII\n")
    f.write("DATASET STRUCTURED_POINTS\n")
    f.write(f"DIMENSIONS {res} {res} {res}\n")
    f.write(f"ORIGIN {x_min} {y_min} {z_min}\n")

    # Calcul de l'espacement entre chaque point
    dx = (x_max - x_min) / (res - 1)
    dy = (y_max - y_min) / (res - 1)
    dz = (z_max - z_min) / (res - 1)
    f.write(f"SPACING {dx} {dy} {dz}\n")
    
    f.write(f"POINT_DATA {res**3}\n")
    f.write("SCALARS humidite float 1\n")
    f.write("LOOKUP_TABLE default\n")
    
    for z in zs:
        for y in ys:
            for x in xs:
                humidite = mon_sol2.getValue(pb.Vector3d(x, y, z))
                f.write(f"{humidite}\n")
print("Champ d'humidité généré !")