import pickle
from ant_colony_algorithm import AntColony

ant_colony = AntColony(num_ants=5, num_nodes=10)
with open('ant_colony.pkl', 'wb') as f:
    pickle.dump(ant_colony, f)
