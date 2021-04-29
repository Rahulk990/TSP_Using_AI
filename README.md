# Travelling Salesman Problem using AI
Travelling Salesman Problem refers to the problem of finding the shortest path that visits N specified locations, starting and ending at the same place and visiting the other destinations exactly once. Even if the TSP’s problem is NP-Hard, it is currently being solved by many transportation companies for routing the deliveries, school bus routes, home service calls, etc. 

Various known optimization algorithms of Artificial Intelligence are implemented to solve the TSP problem. Also, a new Just-a-Look algorithm is devised for the same. 

## _Algorithms Used_
- **2Opt Algorithm:** A Hill Climbing approach to solve the problem
- **Simulated Annealing Algorithm:** Tries to overcome the drawbacks of 2Opt using the concept of annealing in metallurgy
- **Genetic Algorithm:** Based on the process of Natural Selection and Genetics
- **Ant Colony Optimization:** Based on the foraging behaviour of Ants
- **Black Hole Optimization:** Based on the phenomenon of Black Hole in space
- **Just-a-Look Algorithm:** A custom Divide n Conquer Approach for solving the problem by dividing it into sub problems

## _Py Libraries Used_
- **Scikit-Learn:** K-means Clustering of Scikit-Learn is used to divide the problem into sub-problems for the Just-a-Look algorithm
- **Matplotlib:** Used to plot the solution paths for the problem 
