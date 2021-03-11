from random import choices, randrange
import CityManager as cm


class Ant:

    def __init__(self, pheromone_map, alpha, beta):

        self.start_city = randrange(cm.getLength())
        self.possible_cities = [i for i in range(cm.getLength())]

        self.route = []
        self.distance_travelled = 0.0
        self.current_city = self.start_city

        self.alpha = alpha
        self.beta = beta
        self.pheromone_map = pheromone_map

        self.route.append(self.start_city)
        self.possible_cities.remove(self.current_city)

    def selectCity(self):

        city_attraction = []
        total_attraction = 0.0

        for city in self.possible_cities:
            pheromone = self.pheromone_map[self.current_city][city]
            distance = cm.getDistance(self.current_city, city)

            attraction = (pheromone**self.alpha) * ((1/distance)**self.beta)
            city_attraction.append(attraction)
            total_attraction += attraction

        if total_attraction == 0:
            total_attraction = 1

        return choices(
            population=self.possible_cities,
            weights=[attraction/total_attraction for attraction in city_attraction]
        )[0]

    def sendAnt(self):

        # Until Possible Locations is not Empty
        while self.possible_cities:
            next_city = self.selectCity()

            # Update Route
            self.route.append(next_city)
            self.possible_cities.remove(next_city)

            # Update Distance
            self.distance_travelled += cm.getDistance(
                self.current_city, next_city)

            # Update Current Location
            self.current_city = next_city

        self.distance_travelled += cm.getDistance(
            self.current_city, self.start_city)

    def getRoute(self):
        return self.route

    def getDistance(self):
        return self.distance_travelled


class AntManager:

    def __init__(self, colony_size, n_best, alpha, beta, pheromone_evaporation_coefficient, pheromone_constant, iterations):

        # Initializing the List of Ants
        self.ant_count = colony_size
        self.ants = []

        # Initializing Pheromone
        self.tour_size = cm.getLength()
        self.pheromone_map = [
            [0.0]*self.tour_size for _ in range(self.tour_size)]
        self.ant_updated_pheromone_map = [
            [0.0]*self.tour_size for _ in range(self.tour_size)]

        # Other Constants
        self.alpha = alpha
        self.beta = beta
        self.n_best = n_best
        self.pheromone_evaporation_coefficient = pheromone_evaporation_coefficient
        self.pheromone_constant = pheromone_constant
        self.iterations = iterations

        # For Solution
        self.shortest_distance = None
        self.shortest_path = None

    def sendAnts(self):
        for _ in range(self.ant_count):
            ant = Ant(self.pheromone_map, self.alpha, self.beta)
            self.ants.append(ant)
            ant.sendAnt()

    def spreadPheromone(self):
        for start in range(len(self.pheromone_map)):
            for end in range(len(self.pheromone_map)):
                self.pheromone_map[start][end] = (
                    1 - self.pheromone_evaporation_coefficient) * self.pheromone_map[start][end]
                self.pheromone_map[start][end] += self.ant_updated_pheromone_map[start][end]

    def populate_ant_updated_pheromone_map(self, ant):

        route = ant.getRoute()
        for i, city_a in enumerate(route):

            city_b = 0
            if i == len(route) - 1:
                city_b = route[0]
            else:
                city_b = route[i+1]

            new_pheromone_value = self.pheromone_constant/ant.getDistance()
            self.ant_updated_pheromone_map[city_a][city_b] += new_pheromone_value
            self.ant_updated_pheromone_map[city_b][city_a] += new_pheromone_value

    def mainloop(self):

        for _ in range(self.iterations):
            self.sendAnts()

            self.ants = sorted(self.ants, key=lambda ant: ant.getDistance())
            for ant in self.ants[:self.n_best]:
                self.populate_ant_updated_pheromone_map(ant)

                if not self.shortest_distance:
                    self.shortest_distance = ant.getDistance()

                if not self.shortest_path:
                    self.shortest_path = ant.getRoute()

                if ant.getDistance() < self.shortest_distance:
                    self.shortest_distance = ant.getDistance()
                    self.shortest_path = ant.getRoute()

            self.spreadPheromone()
            self.ant_updated_pheromone_map = [
                [0.0]*self.tour_size for _ in range(self.tour_size)]

            if _ % 10 == 0:
                print(f"Iteration: {_} Best Fitness: {self.shortest_distance}")

        return self.shortest_distance, self.shortest_path
