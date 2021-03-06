import Others.City_Manager as cm
from random import shuffle


def getDistance(route) -> int:
    distance = 0
    for i in range(len(route)):
        if i == len(route)-1:
            distance += cm.getDistance(route[i], route[0])
        else:
            distance += cm.getDistance(route[i], route[i+1])

    return distance


class Opt2:

    def __init__(self):

        self.route = []

        # Initializing Random Tour
        for i in range(cm.getLength()):
            self.route.append(i)
        shuffle(self.route)

    def findSolution(self):

        iterations = 0
        while True:

            min_possible = self.getDistance()
            min_route = self.route

            # Checking all the neighbors of the route
            for i in range(len(self.route)):
                for j in range(i, len(self.route)):

                    mutatedRoute = self.route[0:i] + list(
                        reversed(self.route[i:j])) + self.route[j:]

                    # Selecting the best neighbor
                    newDistance = getDistance(mutatedRoute)
                    if newDistance < min_possible:
                        min_possible = newDistance
                        min_route = mutatedRoute

            # Ending scan, if reached a local minima
            if min_route == self.route:
                break

            self.route = min_route
            # print(f"Iteration: {iterations}, Best Value: {min_possible}")
            iterations += 1

        return self.route, iterations

    def getDistance(self):
        return getDistance(self.route)
