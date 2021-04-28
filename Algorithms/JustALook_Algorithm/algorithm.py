import numpy as np
from random import shuffle
import Others.City_Manager as cm
from sklearn.cluster import KMeans


def getDistance(route):
    distance = 0
    for i in range(len(route)):
        if i == len(route)-1:
            distance += cm.getDistance(route[i], route[0])
        else:
            distance += cm.getDistance(route[i], route[i+1])

    return distance


def createRoute(sequence, routes):
    route = []
    for x in sequence:
        route.extend(routes[x])
    return route

# 2Opt used to find Cluster Sequence
def optimizer(numberOfClusters, routes):
    sequence = [x for x in range(numberOfClusters)]
    shuffle(sequence)
    route = createRoute(sequence, routes)

    iterations = 0
    while True:

        min_possible = getDistance(route)
        min_sequence = sequence

        for i in range(len(sequence)):
            for j in range(i, len(sequence)):

                mutatedSequence = sequence[0:i] + list(
                    reversed(sequence[i:j])) + sequence[j:]

                newDistance = getDistance(createRoute(sequence, routes))
                if newDistance < min_possible:
                    min_possible = newDistance
                    min_sequence = mutatedSequence

        if min_sequence == sequence:
            break

        sequence = min_sequence
        iterations += 1

    return createRoute(sequence, routes)


# 2Opt used to solve each Cluster
class Partial_Opt2:

    def __init__(self, initialRoute, isOptimization=False):
        self.route = initialRoute
        if(not isOptimization): shuffle(self.route)

    def findSolution(self):

        iterations = 0
        while True:

            min_possible = self.getDistance()
            min_route = self.route

            for i in range(len(self.route)):
                for j in range(i, len(self.route)):

                    mutatedRoute = self.route[0:i] + list(
                        reversed(self.route[i:j])) + self.route[j:]

                    newDistance = getDistance(mutatedRoute)
                    if newDistance < min_possible:
                        min_possible = newDistance
                        min_route = mutatedRoute

            if min_route == self.route:
                break

            self.route = min_route
            iterations += 1

        return self.route

    def getDistance(self):
        return getDistance(self.route)


class JustALook:

    def __init__(self, clusters):
        self.numberOfClusters = clusters
        self.cities = np.array([city.getCity() for city in cm.cities])

    # Splitting Problem according to Cluster Number
    def partialProblem(self, clusterNumber):
        path = []
        for i in range(cm.getLength()):
            if(self.clusteredCities[i] == clusterNumber):
                path.append(i)
        return path

    # Solving each cluster using 2Opt
    def solvePartialProblem(self, clusterNumber):
        partialRoute = self.partialProblem(clusterNumber)
        solver = Partial_Opt2(partialRoute)
        partialRoute = solver.findSolution()
        return partialRoute

    # Dividing problem into clusters
    def formClusters(self):
        model = KMeans(n_clusters=self.numberOfClusters)
        self.clusteredCities = model.fit_predict(self.cities)

    # Cluster Sequencing
    def solveClusters(self):
        routes = []
        for clusterNumber in range(self.numberOfClusters):
            routes.append(self.solvePartialProblem(clusterNumber))

        solution = optimizer(self.numberOfClusters, routes)
        return solution, getDistance(solution)
