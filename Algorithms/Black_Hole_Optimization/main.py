import time
from Algorithms.Black_Hole_Optimization.algorithm import Black_Hole


def blackHoleOptimization():

    # Configurations
    population_size = 100
    iteration_limit = 300

    BHO = Black_Hole(population_size, iteration_limit)

    startTime = time.time()
    population, _ = BHO.mainloop()
    endTime = time.time()

    time_taken = endTime - startTime
    solution = population[0].tour
    distance = population[0].getDistance()

    return solution, distance, time_taken
