import numpy as np
import plantbox as pb

#gestion des chemins
import os
from pathlib import Path

script_dir = Path(__file__).parent
dossier_simulation = script_dir / "results" / "Augmented_Radius"
os.makedirs(dossier_simulation, exist_ok=True)
parameters_path = f"{script_dir.parent.parent.parent.parent}/modelparameter_TreeCity/structural/Picea_Abies_v2.xml"

"""# 1. Initialisation de la plante
plant = pb.RootSystem()
plant.readParameters(parameters_path)
plant.initialize()

temps_simulation = 2000 # Jours
plant.simulate(temps_simulation)

# 2. Utilisation du SegmentAnalyzer pour extraire les données fiables
# Le SegmentAnalyzer convertit la structure C++ complexe en tableaux Python faciles à lire
ana = pb.SegmentAnalyser(plant)

# Extraction des âges et des types de racines
ages = np.array(ana.getParameter("age"))
subtypes = np.array(ana.getParameter("subType"))

# 3. Création du tableau pour les rayons évolutifs
rayons_evolutifs = np.zeros(len(ages))
taux_epaississement = 0.002 # cm/jour

# 4. Calcul de l'épaississement basé sur le temps
for i in range(len(ages)):
    if subtypes[i] == 1: 
        # Pivot central (subType 1)
        rayon_initial_xml = 0.20 
        rayons_evolutifs[i] = rayon_initial_xml + (ages[i] * taux_epaississement)
        
    elif subtypes[i] == 4 or subtypes[i] == 6:
        # Racines charpentières (subType 4 ou 6)
        rayon_initial_xml = 0.15
        rayons_evolutifs[i] = rayon_initial_xml + (ages[i] * (taux_epaississement / 2))
        
    else:
        # Racines fines (subType 3, 4...) : on ne fait pas d'épaississement
        rayons_evolutifs[i] = 0.05 

# 5. Injection de la nouvelle donnée dans l'Analyzer avant l'export
# On écrase la variable existante "radius" avec notre tableau modifié
ana.addData("radius", rayons_evolutifs.tolist())

# 6. Exportation finale
# On précise explicitement "radius" dans la liste des propriétés à écrire dans le .vtp
ana.write(f"{dossier_simulation}/Picea_Abies_Epaissi.vtp", ["radius", "subType", "age"])

print("Simulation terminée. Fichier VTP généré avec épaississement dynamique des rayons.")"""

# 1. Initialisation de la plante
plant = pb.RootSystem()
plant.readParameters(parameters_path) # Votre fichier XML
plant.initialize()

# Paramètres de l'animation
temps_total = 2000        # Durée totale de la simulation (jours)
pas_de_temps = 5         # On crée une "image" (export VTP) tous les 5 jours
taux_epaississement = 0.002 # Vitesse de croissance radiale (cm/jour)

print("Début de la simulation...")

# 2. Boucle temporelle pour l'animation
# step = numéro de l'image (0, 1, 2...), t = temps actuel de la plante
for step, t in enumerate(range(pas_de_temps, temps_total + pas_de_temps, pas_de_temps)):
    
    # On fait avancer la plante de X jours
    plant.simulate(pas_de_temps)
    
    # On fige la plante à l'instant 't' pour l'analyser
    ana = pb.SegmentAnalyser(plant)
    
    # On récupère le moment EXACT où chaque segment a été créé
    creation_times = np.array(ana.getParameter("creationTime"))
    subtypes = np.array(ana.getParameter("subType"))
    
    # LA CORRECTION MAGIQUE : On calcule l'âge réel du segment à ce moment précis
    # Un segment créé au jour 5, analysé au jour 50, aura 45 jours.
    # L'apex (créé au jour 50) aura 0 jour !
    ages_reels_du_segment = t - creation_times
    
    # On prépare le tableau des rayons
    rayons_evolutifs = np.zeros(len(creation_times))
    
    # 3. Calcul de l'épaississement progressif
    for i in range(len(creation_times)):
        if subtypes[i] == 1: 
            # Pivot : Rayon de base + (âge du segment * taux)
            rayons_evolutifs[i] = 0.20 + (ages_reels_du_segment[i] * taux_epaississement)
            
        elif subtypes[i] == 4 or subtypes[i] == 6:
            # Charpentières : S'épaississent un peu moins vite
            rayons_evolutifs[i] = 0.15 + (ages_reels_du_segment[i] * (taux_epaississement / 2))
            
        else:
            # Racines fines : Ne s'épaississent pas (gardent leur taille de naissance)
            rayons_evolutifs[i] = 0.05 
            
    # On écrase le rayon par défaut avec notre cône parfait
    ana.addData("radius", rayons_evolutifs.tolist())
    
    # 4. Export numéroté pour ParaView (ex: Picea_000.vtp, Picea_001.vtp)
    filename = f"{dossier_simulation}/Picea_Anim_{step:03d}.vtp"
    ana.write(filename, ["radius", "subType", "creationTime"])
    
    print(f"Export de l'étape {step} (Jour {t}) -> {filename}")

print("Simulation terminée avec succès !")