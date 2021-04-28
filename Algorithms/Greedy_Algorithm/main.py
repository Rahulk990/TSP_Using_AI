import time
from Algorithms.Greedy_Algorithm.algorithm import Greedy


# Greedy Algorithm requires no configurations
def greedyAlgorithm():
    greedy = Greedy()

    startTime = time.time()
    greedy.findSolution()
    endTime = time.time()

    time_taken = endTime - startTime
    solution = greedy.getRoute()
    distance = greedy.getDistance()

    return solution, distance, time_taken
