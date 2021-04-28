import time
from Algorithms.Simulated_Annealing.algorithm import Simulated_Annealing 


def simulatedAnnealingAlgorithm():

    # Configurations
    coolingConstant = 0.95
    initialTemperature = 1

    simulatedAnnealing = Simulated_Annealing(coolingConstant, initialTemperature)

    startTime = time.time()
    route, _ = simulatedAnnealing.findSolution()
    endTime = time.time()

    time_taken = endTime - startTime
    solution = route
    distance = simulatedAnnealing.getDistance()

    return solution, distance, time_taken