import numpy as np

class AntColony:
    def __init__(self, num_ants, num_nodes, alpha=1, beta=2, rho=0.5, Q=100):
        self.num_ants = num_ants
        self.num_nodes = num_nodes
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.pheromone = np.ones((num_nodes, num_nodes))
        self.eta = 1 / (np.ones((num_nodes, num_nodes)) + np.eye(num_nodes))
        self.distances = np.full((num_nodes, num_nodes), fill_value=np.inf)
        np.fill_diagonal(self.distances, 0)  # Assuming the diagonal represents the distance from a node to itself

    def run(self, max_iter):
        best_path = None
        all_paths = []
        for i in range(max_iter):
            paths = self.generate_paths()
            self.update_pheromone(paths)
            self.evaporate_pheromone()
            if not best_path or self.calculate_path_cost(paths[0]) < self.calculate_path_cost(best_path):
                best_path = paths[0]
            all_paths.append(best_path)

        return best_path, all_paths

    def generate_paths(self):
        paths = []
        for ant in range(self.num_ants):
            path = []
            visited_nodes = set()
            current_node = np.random.randint(0, self.num_nodes)
            while len(visited_nodes) < self.num_nodes:
                next_node = self.choose_next_node(current_node, visited_nodes)
                path.append((current_node, next_node))
                visited_nodes.add(current_node)
                current_node = next_node
            paths.append(path)
        return paths

    def choose_next_node(self, current_node, visited_nodes):
        pheromone = np.copy(self.pheromone)
        pheromone[list(visited_nodes)] = 0
        row = pheromone[current_node] ** self.alpha * self.eta[current_node] ** self.beta
        probabilities = row / row.sum()
        next_node = np.random.choice(self.num_nodes, 1, p=probabilities)[0]
        return next_node

    def update_pheromone(self, paths):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                delta_pheromone = sum(
                    [self.Q / self.calculate_path_cost(path) for path in paths if (i, j) in path or (j, i) in path])
                self.pheromone[i, j] = (1 - self.rho) * self.pheromone[i, j] + delta_pheromone

    def evaporate_pheromone(self):
        self.pheromone *= self.rho

    def calculate_path_cost(self, path):
        return sum([self.distances[i, j] for i, j in path])

# Example usage:
# ant_colony = AntColony(num_ants=5, num_nodes=10)
# best_path, all_paths = ant_colony.run(max_iter=100)
# print("Best Path:", best_path)
# print("All Paths:", all_paths)
