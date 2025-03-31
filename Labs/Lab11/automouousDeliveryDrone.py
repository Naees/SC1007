"""Q4 Suppose you are programming an autonomous delivery drone that must
deliver packages to multiple locations in a city and return to its starting point
(warehouse). The drone must find the shortest possible route that visits each
delivery location exactly once before returning to the warehouse. Each
location has a distance to every other location. The drone's objective is to
minimize the total travel distance.
Your task is to implement a brute-force approach to find the shortest distance
for the inputs in q4input.txt. Plot the results of execution time for different
inputs and analyze how the execution time increases with the number of
locations. For example, for the following input:
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
The first line indicates the number of locations, which is 4. Each subsequent
line represents the distances from a node to others. For example, 0 10 15 20
mean the distance from node 1 to node 1 is 0, to node 2 is 10, to node 3 is 15,
and to node 4 is 20.
The output will be:
Shortest Distance: 80
Best Route: [0, 1, 3, 2]
Execution Time: 0.00000 sec"""

import itertools
import time
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def read_q4_input(filename):
    """
    Read a TSP input file.
    THe first line is hte numebr of locations.
    Each subsequent line is a row of the distance matrix.
    """
    with open(filename, "r") as file:
        lines = file.read().strip().splitlines()
    n = int(lines[0].strip())
    matrix = []
    for lines in lines[1:]:
        row = list(map(int, lines.split()))
        matrix.append(row)
    return n, matrix

### Part 2: Brute Force TSP Solution ###

def tsp_bruteforce(n, matrix):
    """
    Solves the TSP using brute force.
    We assume the starting point is node 0.
    Returns the best (shortest) total distance and the corresponding route.
    """
    node = list(range(n))
    best_distance = float("inf")
    best_route = None
    # Fix the starting point a node 0 and permute the remaining nodes.
    for perm in itertools.permutations(node[1:]):
        # Create a route that starts and ends at 0.
        route = (0,) + perm + (0,)
        # Calculate the total distance for this route
        total_distance = sum(matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        if total_distance < best_distance:
            best_distance = total_distance
            best_route = route
    return best_distance, best_route

if __name__ == "__main__":
    # Process a single TSP instance form file:
    filename = "q4input.txt"
    n, matrix = read_q4_input(filename)
    
    print(f"Number of locations: {n}")
    print("Distance Matrix:")
    for row in matrix:
        print(row)
    
    start_time = time.time()
    best_distance, best_route = tsp_bruteforce(n, matrix)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("\n--- TSP Result from File Input ---")
    print(f"Shortest Distance: {best_distance}")
    print(f"Best Rout: {best_route[:-1]}")
    print(f"Execution TIme: {execution_time:.5f} sec")
    
    def generate_random_tsp(n, max_distance=100):
        # Create a symmetric distance matrix with zeros on the diagonal.
        matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                dist = random.randint(1, max_distance)
                matrix[i][j] = dist
                matrix[j][i] = dist
        return matrix
    
    # Test with various numbers of locations (keeping n small because factorial time grows very fast)
    location_counts = [4, 5, 6, 7, 8]
    exec_times = []
    
    for count in location_counts:
        matrix_random = generate_random_tsp(count)
        start = time.time()
        tsp_bruteforce(count, matrix_random)
        exec_times.append(time.time() - start)
        print(f"Locations: {count}, Execution Time: {exec_times[-1]:.5f} sec")
    
    # Plot the execution times
    plt.figure(figsize=(10,6))
    plt.plot(location_counts, exec_times, marker='o', linestyle='-')
    plt.xlabel("Number of Locations")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Brute Force TSP Execution Time vs. Number of Locations")
    plt.grid(True)
    plt.show()