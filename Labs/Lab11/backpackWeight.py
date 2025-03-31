from itertools import chain, combinations
import time
import random
import matplotlib
matplotlib.use('TkAgg')  # Use an interactive Tk-based backend
import matplotlib.pyplot as plt
import tkinter


# Q3 Suppose you are a treasure hunter exploring an ancient cave filled with
# valuable artifacts. You have a backpack with a limited weight capacity W,
# and you must decide which artifacts to take to maximize your total value.
# Each artifact has a weight wi (how heavy it is) and a value vi (how much
# gold it’s worth). However, you cannot take a fraction of an artifact, i.e., you
# must take either the whole artifact or leave it behind. Your goal is to
# maximize the total value of your loot while staying within the weight limit
# of your backpack.
# Implement a brute force approach to try all possible subsets of artifacts.
# Measure execution time for different backpack capacities and artifacts
# values and weights shown in q3input.txt. Plot the results of execution time
# for different inputs and analyze how the execution time increases with the
# number of artifacts. For example, for the following input:
# 50
# 10 60
# 20 100
# 30 120
# 5 30
# 15 80
# The first line indicates the backpack's capacity, which is 60. Each
# subsequent line represents an artifact's weight and value. For example,
# artifact 1 has a weight of 10 and a value of 60. In total, there are 5 artifacts.
# The output will be:
# Maximum Value: 270
# Selected Items (weight, value): [(10, 60), (20, 100), (5, 30), (15, 80)]
# Total Weight Used: 50
# Execution Time: 0.00000 sec

def all_subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) +1))

def knapsack(W, artifacts):
    max_value = 0
    best_subset = None
    for subset in all_subsets(artifacts):
        total_weight = sum(item[0] for item in subset)
        total_value = sum(item[1] for item in subset)
        if total_weight <= W and total_value > max_value:
            max_value = total_value
            best_subset = subset
    return max_value, best_subset

def read_input_file(filename):
    with open(filename, "r") as file:
        data = file.read().strip()
    test_case = data.split("\n\n")
    cases = []
    for case in test_case:
        lines = case.strip().splitlines()
        if not lines:
            continue
        # The first line is the backpack capacity
        capacity = int(lines[0])
        artifacts = []
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2:
                weight, value = map(int, parts)
                artifacts.append((weight, value))
        cases.append((capacity, artifacts))
    return cases
                

if __name__ == "__main__":
    # --- PART 1: use the provided file input ---
    filename = "q3input.txt"
    cases = read_input_file(filename)
    
    # List to store results for plotting
    execution_times = []
    artifact_counts = []
    
    print("Processing test cases from file...\n")
    for idx, (capacity, artifacts) in enumerate(cases):
        print(f"Test case {idx+1}: Capacity = {capacity}, Number of artifacts = {len(artifacts)}")
        start_time = time.time()
        max_value, best_subset = knapsack(capacity, artifacts)
        end_time = time.time()
        exec_time = end_time - start_time
        
        execution_times.append(exec_time)
        artifact_counts.append(len(artifacts))
        
    
    # --- PART 2: Plotting the execution time results ---
    
    plt.figure(figsize=(10,6))
    plt.plot(artifact_counts, execution_times, marker='o')
    plt.xlabel("Number of Artifacts")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Brute Force Knapsack: Execution Time vs. Number of Artifacts")
    plt.grid(True)
    plt.show()