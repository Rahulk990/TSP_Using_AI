from random import choices, random, randrange

from Others.Tour import Tour
from Algorithms.Genetic_Algorithm.algorithm import Population


# Selection Methods
def weighted_Selection(population: Population) -> Tour:
    return choices(
        population=population.tours,
        weights=[tour.getFitness() for tour in population.tours]
    )[0]


def tournament_Selection(tournament_size: int, population: Population) -> Tour:
    tournament = Population(tournament_size, False)

    for i in range(tournament_size):
        randomId = randrange(0, population.getSize())
        tournament.setTour(i, population.getTour(randomId))

    tournament.sortPopulation()
    return tournament.tours[0]


# Crossover Function
def ordered_crossover(parent_a: Tour, parent_b: Tour) -> Tour:

    # New Child
    offspring = Tour()

    # Getting Sub-tour
    startpos = randrange(0, parent_a.getSize())
    endpos = randrange(0, parent_a.getSize())

    if(startpos > endpos):
        startpos, endpos = endpos, startpos

    for i in range(offspring.getSize()):
        if i > startpos and i < endpos:
            offspring.setCity(i, parent_a.getCity(i))
        else:
            offspring.setCity(i, None)

    for i in range(offspring.getSize()):
        if not offspring.containsCity(parent_b.getCity(i)):

            for j in range(0, offspring.getSize()):
                if offspring.getCity(j) == None:
                    offspring.setCity(j, parent_b.getCity(i))
                    break

    return offspring


# Mutation Function
def swap_Mutation(mutationRate: float, tour: Tour) -> Tour:
    for i, city in enumerate(tour.tour):
        if random() <= mutationRate:

            # Getting second random city
            randomId = randrange(0, tour.getSize())
            other_city = tour.getCity(randomId)

            # Swapping the Route
            tour.setCity(i, other_city)
            tour.setCity(randomId, city)

    return tour


def reverse_sequence_Mutation(mutationRate: float, tour: Tour) -> Tour:

    # Mutated Child
    mutated = Tour()

    # Getting Sub-tour
    startpos = randrange(0, tour.getSize())
    endpos = randrange(0, tour.getSize())

    if(startpos > endpos):
        startpos, endpos = endpos, startpos

    mutated.tour = tour.tour[0:startpos] + \
        list(reversed(tour.tour[startpos:endpos])) + tour.tour[endpos:]
    return mutated
