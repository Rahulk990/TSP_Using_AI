import matplotlib.pyplot as plt
import Others.City_Manager as cm


def plotProblem():

    # Getting Coordinates of the cities
    points = [city.getCity() for city in cm.cities]

    x, y = [], []
    for point in points:
        x.append(point[0])
        y.append(point[1])

    # Plotting points
    plt.plot(x, y, 'co', color='red')

    # Other configurations
    plt.xlim(0, max(x)*1.1)
    plt.ylim(0, max(y)*1.1)
    plt.show()


def plotSolution(path):

    # Getting Coordinates of the cities
    points = [city.getCity() for city in cm.cities]

    x, y = [], []
    for i in path:
        x.append(points[i][0])
        y.append(points[i][1])

    # Plotting points
    plt.plot(x, y, 'co', color='red')

    # Plotting the solution
    a_scale = float(max(x))/float(100)
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]),
              head_width=a_scale, color='blue', length_includes_head=True)
    for i in range(0, len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]),
                  head_width=a_scale, color='blue', length_includes_head=True)

    # Other configurations
    plt.xlim(0, max(x)*1.1)
    plt.ylim(0, max(y)*1.1)
    plt.show()
