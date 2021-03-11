from Tour import Tour
from typing import List, Tuple
from random import choices, random, randrange


class Population:

    def __init__(self, size: int, initialize: bool) -> None:
        # Holds Population of Tours
        self.tours: List[Tour] = []

        # Initializing Population
        if initialize:
            self.tours = [Tour() for _ in range(size)]
        else:
            self.tours = [None for _ in range(size)]

    def setPopulation(self, new_population: List[Tour]):
        self.tours = new_population

    def setTour(self, index: int, tour: Tour) -> None:
        self.tours[index] = tour

    def getTour(self, index: int) -> Tour:
        return self.tours[index]

    def getSize(self) -> int:
        return len(self.tours)

    def sortPopulation(self) -> None:
        self.tours = sorted(
            self.tours, key=lambda tour: tour.getFitness(), reverse=True)


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
    
    mutated.tour = tour.tour[0:startpos] + list(reversed(tour.tour[startpos:endpos])) + tour.tour[endpos:]
    return mutated


def evolvePopulation(
    population_size: int,
    elitism_offset: int,
    selection_func,
    crossover_func,
    mutation_func,
    generation_limit: int
) -> Tuple[Population, int]:

    generation = Population(population_size, True)
    generation.sortPopulation()

    for i in range(generation_limit):

        # Holds the Next Generation
        next_generation = Population(population_size, False)

        # Implement Elitism
        for j in range(elitism_offset):
            next_generation.setTour(j, generation.getTour(j))

        # Implement Crossover
        for j in range(elitism_offset, generation.getSize()):

            # Select Parents
            parent_a = selection_func(generation)
            parent_b = selection_func(generation)

            # Crossover Parents
            offspring = crossover_func(parent_a, parent_b)

            # Mutation
            offspring = mutation_func(offspring)

            # Adding Tour to New Generation
            next_generation.setTour(j, offspring)

        generation = next_generation
        generation.sortPopulation()

        if i%10 == 0:
            print(f"Generation: {i} Best Fitness: {generation.tours[0].getDistance()}")

    return generation, i
