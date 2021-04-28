import time
from Algorithms.Ant_Colony_Optimization.algorithm import AntManager


def antColonyOptimization():

    # Configurations
    colony_size = 100
    n_best = 60
    alpha = 1
    beta = 1.2
    pheromone_evaporation_coefficient = 0.25
    pheromone_constant = 1
    iterations = 300

    ACO = AntManager(
        colony_size=colony_size,
        n_best=n_best,
        alpha=alpha,
        beta=beta,
        pheromone_evaporation_coefficient=pheromone_evaporation_coefficient,
        pheromone_constant=pheromone_constant,
        iterations=iterations
    )

    startTime = time.time()
    shortest_distance, shortest_path = ACO.mainloop()
    endTime = time.time()

    time_taken = endTime - startTime
    solution = shortest_path
    distance = shortest_distance

    return solution, distance, time_taken
