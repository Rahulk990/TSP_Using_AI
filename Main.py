from Genetic_Algorithm import evolvePopulation, ordered_crossover, reverse_sequence_Mutation, swap_Mutation, tournament_Selection
from Greedy_Algorithm import Greedy
from City import City
import CityManager as cm
from functools import partial
import time
from Plotter import plotTSP, plotPoints
from Ant_Colony_Opt import AntManager
from Hill_Climbing import Hill_Climbing
from Simulated_Annealing import Simulated_Annealing
import csv


def initializeProblem():
    cm.clear()

    # with open('kro100.txt') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=' ')
    #     for row in csv_reader:
    #         cm.addCity(City(float(row[1]), float(row[2])))

    for _ in range(60):
        cm.addCity(City())

    cm.calculateDistances()


def plotProblem():
    points = [city.getCity() for city in cm.cities]
    plotPoints(points)


def plotSolution(path):
    points = [city.getCity() for city in cm.cities]
    plotTSP([path], points, 1)


def greedyAlgorithm():

    greedy = Greedy()

    startTime = time.time()
    greedy.findSolution()
    endTime = time.time()

    print(f"Time taken: {endTime - startTime}s")
    print(f"Solution: {greedy.getRoute()}")
    print(f"Distance: {greedy.getDistance()}")

    plotSolution(greedy.getRoute())


def geneticAlgorithm():

    population_size = 50
    elitism_offset = 5
    generation_limit = 800

    selectionFunc = partial(tournament_Selection, 35)
    crossoverFunc = partial(ordered_crossover)
    mutationFunc = partial(reverse_sequence_Mutation, 0.01)

    startTime = time.time()
    population, generations = evolvePopulation(
        population_size=population_size,
        elitism_offset=elitism_offset,
        selection_func=selectionFunc,
        crossover_func=crossoverFunc,
        mutation_func=mutationFunc,
        generation_limit=generation_limit
    )
    endTime = time.time()

    print(f"Number of Generations: {generations}")
    print(f"Time taken: {endTime - startTime}s")
    print(
        f"Best Solution: {population.tours[0].tour}, {population.tours[0].getDistance()}")

    plotSolution(population.tours[0].tour)


def antColonyAlgorithm():

    colony_size = 50
    n_best = 30
    alpha = 1
    beta = 1.2
    pheromone_evaporation_coefficient = 0.25
    pheromone_constant = 10
    iterations = 400

    ACO = AntManager(
        colony_size=colony_size,
        n_best=n_best,
        alpha=alpha,
        beta=beta,
        pheromone_evaporation_coefficient=pheromone_evaporation_coefficient,
        pheromone_constant=pheromone_constant,
        iterations=iterations
    )

    startTime = time.time()
    shortest_distance, shortest_path = ACO.mainloop()
    endTime = time.time()

    print(f"Time taken: {endTime - startTime}s")
    print(f"Best Solution: {shortest_path}, {shortest_distance}")

    plotSolution(shortest_path)


def hillClimbingAlgorithm():

    solution = Hill_Climbing()

    startTime = time.time()
    route, generations = solution.findSolution()
    endTime = time.time()

    print(f"Number of Generations: {generations}")
    print(f"Time taken: {endTime - startTime}s")
    print(f"Best Solution: {route}, {solution.getDistance()}")

    plotSolution(route)


def simulatedAnnealingAlgorithm():

    solution = Simulated_Annealing(0.99, 1)

    startTime = time.time()
    route, generations = solution.findSolution()
    endTime = time.time()

    print(f"Number of Generations: {generations}")
    print(f"Time taken: {endTime - startTime}s")
    print(f"Best Solution: {route}, {solution.getDistance()}")

    plotSolution(route)


if __name__ == '__main__':

    initializeProblem()

    plotProblem()

    greedyAlgorithm()

    hillClimbingAlgorithm()

    simulatedAnnealingAlgorithm()

    geneticAlgorithm()

    antColonyAlgorithm()
