import random
import string


target_string= 'geneticalgorithm'

# num_of_generations
generations = 1000

# population_size 
population_size = 100

# mutation_rate 
mutation_rate = 0.01

# random generation for the first generation 
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length) )


# fitness calculation 
def calculate_fitness(individual):
    return sum(1 for a,b in zip(individual, target_string) if a == b)

# crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent2[crossover_point:]
    return child1, child2


# mutation 
def mutate(individual):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.uniform(0,1) < mutation_rate:
            mutated_individual[1] = random.choice(string.ascii_lowercase)
    return ''.join(mutated_individual)


population = [generate_random_string(len(target_string)) for _ in range(population_size)]

for generation in range(generations):
    fitness_scores = [calculate_fitness(individual) for individual in population]

    parents = random.choices(population, weights = fitness_scores, k=2)
    offspring = crossover(parents[0], parents[1])

    offspring = [mutate(child) for child in offspring]

    min_fitness_index = fitness_scores.index(min(fitness_scores))
    population[min_fitness_index:min_fitness_index+2] = offspring

    if target_string in population:
        print("Target string '{}' reached in generation {}".format(target_string, generation + 1))
        break

print('Final population')
print(population)