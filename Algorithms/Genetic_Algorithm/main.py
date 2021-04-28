import time
from functools import partial

from Algorithms.Genetic_Algorithm.algorithm import evolvePopulation
from Algorithms.Genetic_Algorithm.functions import tournament_Selection, ordered_crossover, reverse_sequence_Mutation

def geneticAlgorithm():

    # Configurations
    population_size = 100
    elitism_offset = 5
    generation_limit = 500

    # These functions also have alternatives present in functions.py
    selectionFunc = partial(tournament_Selection, 30)
    crossoverFunc = partial(ordered_crossover)
    mutationFunc = partial(reverse_sequence_Mutation, 0.01)


    startTime = time.time()
    population, _ = evolvePopulation(
        population_size=population_size,
        elitism_offset=elitism_offset,
        selection_func=selectionFunc,
        crossover_func=crossoverFunc,
        mutation_func=mutationFunc,
        generation_limit=generation_limit
    )
    endTime = time.time()

    time_taken = endTime - startTime
    solution = population.tours[0].tour
    distance = population.tours[0].getDistance()

    return solution, distance, time_taken