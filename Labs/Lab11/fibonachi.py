import matplotlib.pyplot as plt
import time

# 2 Try the recursive and iterative Fibonacci. Measure execution time for
# different n values (e.g., 20, 30, 40, 45). Plot the results of execution time for
# different input. What is the time complexity for each algorithm?

def recursive_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def iterative_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for _ in range(3, n + 1):
        c = a+b
        b = a
        a = c
    return c

if __name__ == "__main__":
    input = [20, 30, 40, 45]
    recursive_times = []
    interative_times = []
    
    for n in input:
        # iterative fib analysis
        start_time = time.time()
        iterative_fibonacci(n)
        end_time = time.time()
        interative_times.append(end_time - start_time)
        
        # recursive fib analysis
        start_time = time.time()
        recursive_fibonacci(n)
        end_time = time.time()
        recursive_times.append(end_time - start_time)
        
        print(f"n = {n}")
        print(f" Recursive Fibonacci Time: {recursive_times[-1]:.4f} seconds")
        print(f"Iterative Fibonacci TIme: {interative_times[-1]:.4f} seconds")
        print("-"*40)
    
    plt.figure(figsize=(10,6))
    plt.plot(input, recursive_times, label="Recursive Fibonacci", marker='o')
    plt.plot(input, interative_times, label="Iterative Fibonacci", marker='o')
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time Comparison: Recursive vs. Iterative Fibonacci")
    plt.legend()
    plt.grid(True)
    plt.show()
    
# Time Complexity Analysis

#     Recursive Fibonacci:

#         Implementation:
#         The recursive function calls itself twice for each non-base case:

#     return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

#     Time Complexity:
#     This results in an exponential number of calls, with a time complexity of approximately O(2n)O(2n) (more precisely, O(ϕn)O(ϕn) where ϕ≈1.618ϕ≈1.618 is the golden ratio).

#     Implication:
#     As nn increases, the execution time grows exponentially. Even moderate increases in nn can lead to drastically longer runtimes.

# Iterative Fibonacci:

#     Implementation:
#     The iterative function uses a loop from 3 to nn to build the sequence:

#         for _ in range(3, n + 1):
#             c = a + b
#             b = a
#             a = c

#         Time Complexity:
#         This method runs in linear time, O(n)O(n), because it performs a constant amount of work for each value of nn.

#         Implication:
#         The iterative approach scales much better with increasing nn, leading to significantly lower execution times compared to the recursive version for large nn.

# Summary

#     Recursive Fibonacci: Exponential time complexity O(2n)O(2n), which makes it very inefficient as nn increases.

#     Iterative Fibonacci: Linear time complexity O(n)O(n), which makes it much more efficient and scalable.

# By running the above script, you will see that the recursive method becomes extremely slow as nn increases (especially noticeable at n=40n=40 and n=45n=45), while the iterative method remains relatively fast. This practical experiment illustrates why the iterative (or optimized recursive with memoization) approach is preferred for calculating Fibonacci numbers for large inputs.
