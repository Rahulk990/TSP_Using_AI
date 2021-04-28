import time
from Algorithms.Opt2_Algorithm.algorithm import Opt2


# 2Opt Algorithm requires no configurations
def opt2Algorithm():

    opt2 = Opt2()

    startTime = time.time()
    route, _ = opt2.findSolution()
    endTime = time.time()

    time_taken = endTime - startTime
    solution = route
    distance = opt2.getDistance()

    return solution, distance, time_taken
