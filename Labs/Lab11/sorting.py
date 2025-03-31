import random
import time
import matplotlib.pyplot as plt

# Q1 Given an array of n elements, try Bubble Sort and Merge Sort, and compare
# their execution times for different input sizes. You can generate an array of
# random numbers (e.g., size 1,000, 10,000, 100,000). Use the time module of
# Python to measure execution time. Plot the results of execution time for
# different input sizes.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
if __name__ == "__main__":
    input_sizes = [1000, 10000, 1000000]
    bubble_times = []
    merge_times = []
    
    for n in input_sizes:
        arr = [random.randint(0, n) for _ in range (n)]
        arr_copy = arr.copy()
        start_time = time.time()
        bubble_sort(arr_copy)
        end_time = time.time()
        result_time = end_time - start_time
        bubble_times.append(result_time)
        
        arr_copy = arr.copy()
        start_time = time.time()
        merge_sort(arr_copy)
        end_time = time.time()
        result_time = end_time - start_time
        merge_times.append(result_time)
        
        print(f"Input Size: {n}")
        print(f" Bubble Sort Time: {bubble_times[-1]:.4f} seconds")
        print(f" Merge Sort Time: {merge_times[-1 ]:.4f} seconds")
        print("-" * 40)
    
    plt.figure(figsize=(10,6))
    plt.plot(input_sizes, bubble_times, label="Bubble Sort", marker='o')
    plt.plot(input_sizes, merge_times, label="Merge Sort", marker='o')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution TIme (seconds)')
    plt.title('Execution TIme Comparison: Bubble Sort vs. Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    