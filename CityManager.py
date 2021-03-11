from typing import List
from City import City

cities: List[City] = []
distances: List[List[float]] = []


def addCity(city: City) -> None:
    cities.append(city)


def getCity(index: int) -> City:
    return cities[index]


def getLength() -> int:
    return len(cities)


def calculateDistances() -> None:
    for start in cities:

        distances_from_start = []
        for end in cities:
            xDiff = abs(start.getCity()[0] - end.getCity()[0])
            yDiff = abs(start.getCity()[1] - end.getCity()[1])
            distances_from_start.append((xDiff**2 + yDiff**2)**0.5)

        distances.append(distances_from_start)


def getDistance(index_a: int, index_b: int) -> float:
    return distances[index_a][index_b]


def clear():
    cities.clear()
    distances.clear()
