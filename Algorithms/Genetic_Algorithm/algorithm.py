from Others.Tour import Tour
from typing import List, Tuple


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

        # if i%10 == 0:
        #     print(f"Generation: {i} Best Fitness: {generation.tours[0].getDistance()}")

    return generation, i
