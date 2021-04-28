import math
from random import random, randrange, shuffle
import Others.City_Manager as cm


def getDistance(route) -> int:
    distance = 0
    for i in range(len(route)):
        if i == len(route)-1:
            distance += cm.getDistance(route[i], route[0])
        else:
            distance += cm.getDistance(route[i], route[i+1])

    return distance


class Simulated_Annealing:

    def __init__(self, beta, initial_temperature):

        self.beta = beta
        self.temperature = initial_temperature
        self.route = []

        # Initializing Random Tour
        for i in range(cm.getLength()):
            self.route.append(i)
        shuffle(self.route)

    def findSolution(self):

        min_possible = self.getDistance()
        min_route = self.route

        iterations = 0
        iterations2 = 0
        while self.temperature > 1e-4:

            energy = min_possible

            mutatedRoute = None
            if random() < 0.5:

                startpos = randrange(0, len(self.route))
                endpos = randrange(0, len(self.route))

                if(startpos > endpos):
                    startpos, endpos = endpos, startpos

                mutatedRoute = self.route[0:startpos] + list(
                    reversed(self.route[startpos:endpos])) + self.route[endpos:]

            else:

                mutatedRoute = self.route.copy()

                startpos = randrange(0, len(self.route))
                endpos = randrange(0, len(self.route))

                mutatedRoute[startpos] = self.route[endpos]
                mutatedRoute[endpos] = self.route[startpos]

            new_energy = getDistance(mutatedRoute)

            try:
                if random() < math.exp(- (new_energy - min_possible) / self.temperature):
                    energy = new_energy
                    self.route = mutatedRoute

                    if energy < min_possible:
                        min_possible = energy
                        min_route = mutatedRoute

                    iterations += 1
                    if iterations % 100 == 0:
                        self.temperature *= self.beta

                    # if iterations % 100 == 0:
                    #     print(
                    #         f"Iteration: {iterations}, Temperature: {self.temperature},  Best Value: {min_possible}")

            except:
                pass

            iterations2 += 1
            if iterations2 == 1000000:
                break

        return min_route, iterations

    def getDistance(self):
        return getDistance(self.route)
