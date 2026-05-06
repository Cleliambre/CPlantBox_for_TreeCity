import plantbox as pb

plant = pb.Plant()
path = "../../modelparameter_TreeCity/structural/Picea_Abies_v2"
plant.readParameters(path + ".xml")

# Initialize
plant.initialize()

# Simulate
sim_time = 5000
dt = 50
n_steps = round(sim_time / dt)
for i in range(0, n_steps):
    plant.simulate(dt)
    plant.write("results/Picea_Abies_" + str(i) + ".vtp")


