import csv

# Other Modules
import Others.City_Manager as cm
from Others.City import City
from Others.Graph_Plotter import plotProblem, plotSolution

# Algorithms
from Algorithms.Greedy_Algorithm.main import greedyAlgorithm
from Algorithms.Opt2_Algorithm.main import opt2Algorithm
from Algorithms.Simulated_Annealing.main import simulatedAnnealingAlgorithm
from Algorithms.Genetic_Algorithm.main import geneticAlgorithm
from Algorithms.Ant_Colony_Optimization.main import antColonyOptimization
from Algorithms.Black_Hole_Optimization.main import blackHoleOptimization
from Algorithms.JustALook_Algorithm.main import justALookAlgorithm


def loadDataset(datasetName):
    cm.clear()

    # Creating the Random Problem
    if (datasetName[0:6] == 'Random'):
        for _ in range(int(datasetName[7:])):
            cm.addCity(City())

    # Loading the given Dataset
    else:
        with open('Data/' + datasetName + '.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            for row in csv_reader:
                cm.addCity(City(float(row[0]), float(row[1])))

    # Pre-calculating Distances
    cm.calculateDistances()


if __name__ == '__main__':

    # Put the dataset name here
    # Put 'Random-X' for random generation of X-city problem
    datasetName = 'Random-50'
    loadDataset(datasetName)

    # Plotting the Problem
    plotProblem()

    # Applying Algorithms
    # Each algorithm will return 3-Tuple (Solution, Distance, Time Taken)
    # Note: For changing algorithm parameters, check their main.py

    # Greedy Algorithm
    greedy = greedyAlgorithm()
    plotSolution(greedy[0])
    print(f'Distance: {greedy[1]}, Time: {greedy[2]}')

    # 2Opt Algorithm
    opt2 = opt2Algorithm()
    plotSolution(opt2[0])
    print(f'Distance: {opt2[1]}, Time: {opt2[2]}')

    # Simulated_Annealing
    simulatedAnnealing = simulatedAnnealingAlgorithm()
    plotSolution(simulatedAnnealing[0])
    print(f'Distance: {simulatedAnnealing[1]}, Time: {simulatedAnnealing[2]}')

    # Genetic Algorithm
    genetic = geneticAlgorithm()
    plotSolution(genetic[0])
    print(f'Distance: {genetic[1]}, Time: {genetic[2]}')

    # Ant Colony Optimization
    antColony = antColonyOptimization()
    plotSolution(antColony[0])
    print(f'Distance: {antColony[1]}, Time: {antColony[2]}')

    # Black Hole Optimization
    blackHole = blackHoleOptimization()
    plotSolution(blackHole[0])
    print(f'Distance: {blackHole[1]}, Time: {blackHole[2]}')

    # Just-a-Look Algorithm
    justALook = justALookAlgorithm()
    plotSolution(justALook[0])
    print(f'Distance: {justALook[1]}, Time: {justALook[2]}')
