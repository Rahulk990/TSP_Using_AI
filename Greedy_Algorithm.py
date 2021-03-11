import CityManager as cm
from random import randrange


class Greedy:

    def __init__(self):

        self.startCity: int = randrange(cm.getLength())
        self.possibleCities = [i for i in range(cm.getLength())]

        self.route = []
        self.distanceTravelled = 0.0
        self.currentCity = self.startCity

        self.route.append(self.startCity)
        self.possibleCities.remove(self.currentCity)

    def selectCity(self):

        nearestCity = self.possibleCities[0]
        nearestCityDistance = cm.getDistance(self.currentCity, nearestCity)

        for city in self.possibleCities:

            distanceFromCity = cm.getDistance(self.currentCity, city)
            if distanceFromCity < nearestCityDistance:
               nearestCity = city
               nearestCityDistance = distanceFromCity

        return nearestCity

    def findSolution(self):

        # Until Possible Locations is not Empty
        while self.possibleCities:
            nextCity = self.selectCity()

            # Update Route
            self.route.append(nextCity)
            self.possibleCities.remove(nextCity)

            # Update Distance
            self.distanceTravelled += cm.getDistance(self.currentCity, nextCity)

            # Update Current Location
            self.currentCity = nextCity

        self.distanceTravelled += cm.getDistance(self.currentCity, self.startCity)

    def getRoute(self):
        return self.route

    def getDistance(self):
        return self.distanceTravelled
