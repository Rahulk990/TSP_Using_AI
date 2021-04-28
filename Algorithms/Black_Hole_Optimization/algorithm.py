from Others.Tour import Tour
from random import randrange


class Black_Hole:

    def __init__(self, population_size, iteration_limit):

        # Store the stars
        self.population_size = population_size
        self.tours = [Tour() for _ in range(population_size)]

        # Max Iterations
        self.iteration_limit = iteration_limit

    def setTour(self, index: int, tour: Tour) -> None:
        self.tours[index] = tour

    def getTour(self, index: int) -> Tour:
        return self.tours[index]

    def getSize(self) -> int:
        return len(self.tours)

    def sortPopulation(self) -> None:
        self.tours = sorted(
            self.tours, key=lambda tour: tour.getFitness(), reverse=True)

    def moveCloser(self, blackHole, star):

        min_possible = star.getDistance()
        min_tour = star

        for i in range(7):
            # New Child
            newStar = Tour()

            # Getting Sub-tour
            startpos = randrange(0, blackHole.getSize())
            endpos = randrange(0, blackHole.getSize())

            if(startpos > endpos):
                startpos, endpos = endpos, startpos

            for i in range(newStar.getSize()):
                if i > startpos and i < endpos:
                    newStar.setCity(i, blackHole.getCity(i))
                else:
                    newStar.setCity(i, None)

            for i in range(newStar.getSize()):
                if not newStar.containsCity(star.getCity(i)):
                    for j in range(0, newStar.getSize()):
                        if newStar.getCity(j) == None:
                            newStar.setCity(j, star.getCity(i))
                            break
            
            if(newStar.getDistance(True) < min_possible):
                return newStar

        return min_tour

    def mainloop(self):

        self.sortPopulation()
        for i in range(self.iteration_limit):

            blackHole = self.tours[0]
            # Moving Stars toward the Black Hole
            for j in range(1, self.population_size):
                newStar = self.moveCloser(blackHole, self.tours[j])
                self.setTour(j, newStar)

            # Checking for Event Horizon
            blackHole_value = 1/self.tours[0].getDistance()
            sumValues = [1/self.tours[j].getDistance() for j in range(1, self.population_size)]

            # Deaths of stars
            radius = blackHole_value/sum(sumValues)
            for j in range(1, self.population_size):
                if(abs(self.tours[j].getDistance() - blackHole_value) < radius):
                    self.setTour(j, Tour())

            self.sortPopulation()
            if i % 10 == 0:
                print(f"Generation: {i} Best Fitness: {self.tours[0].getDistance()}")

        return self.tours, i
