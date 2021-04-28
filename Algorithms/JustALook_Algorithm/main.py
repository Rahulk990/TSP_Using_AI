import time
from Algorithms.JustALook_Algorithm.algorithm import JustALook

def justALookAlgorithm():

    # Configurations
    number_of_clusters = 3
    
    JL = JustALook(number_of_clusters)

    startTime = time.time()
    JL.formClusters()
    path, pathDistance = JL.solveClusters()
    endTime = time.time()

    time_taken = endTime - startTime
    solution = path
    distance = pathDistance

    return solution, distance, time_taken