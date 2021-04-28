from typing import List
from random import shuffle
import Others.City_Manager as cm


class Tour:

    def __init__(self) -> None:
        # Holds a candidate Solution
        self.tour: List[int] = []

        # Caching
        self.fitness: float = 0
        self.distance: int = 0

        # Initializing Random Tour
        for i in range(cm.getLength()):
            self.tour.append(i)
        shuffle(self.tour)

    def getCity(self, index: int) -> int:
        return self.tour[index]

    def setCity(self, index: int, city: int) -> None:
        self.tour[index] = city

        # Tour Altered, Cache needs to be reset
        self.fitness = 0
        self.distance = 0

    def containsCity(self, city: int) -> bool:
        return (city in self.tour)

    def getFitness(self) -> float:
        if self.fitness == 0:
            self.fitness = 1/self.getDistance()
        return self.fitness

    def getDistance(self, fresh=False) -> int:
        if self.distance == 0 or fresh:
            for i in range(len(self.tour)):
                if i == len(self.tour)-1:
                    self.distance += cm.getDistance(self.tour[i], self.tour[0])
                else:
                    self.distance += cm.getDistance(
                        self.tour[i], self.tour[i+1])

        return self.distance

    def getSize(self) -> int:
        return len(self.tour)
