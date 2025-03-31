import time

def dual_search(A, size, k, dual_index):
    """
    Searches the array A for two elements whose sum equals K.
    The two elements can be the same element.
    Once a valid pair is found, their indices are stored in dual_index and the function terminates.
    
    Parameters:
      A (list): The input array of integers.
      size (int): The number of elements in A.
      K (int): The target sum.
      dual_index (list): A list to store the indices of the found pair.
    """
    
    # Loop over each element in A.
    for i in range(size):
        # The inner loop start at i so that the same element can be chosen twice
        for j in range(i, size):
            # Check if the sum of the pair equals K.
            if A[i] + A[j] == k:
                dual_index.append(i)
                dual_index.append(j)
                print(f"Pair found at indices: {dual_index}")
                print(f"Elements: {A[i]} + {A[j]} = {K}")
                return  # Exit as soon as a valid pair is found.
    print("dual_search: No pair found for K =", K)

            
def dual_sorted_search(A, size, K, dual_index):
    left = 0
    right = size-1
    
    while left <= right:
        current_sum = A[left] + A[right]
        
        if current_sum == K:
            dual_index.append(left)
            dual_index.append(right)
            print(f"Pair found at indices: {dual_index}")
            print(f"Elements: {A[left]} + {A[right]} = {K}")
            return
        
        elif current_sum < K:
            left+=1
        elif current_sum > K:
            right-=1
    print("dual_sorted_search: No pair found for K =", K)


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

def read_input(filename):
    """
    Read the input file and returns the search key, data size, and the list of data.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    K = int(lines[0].strip())
    data_size = int(lines[1].strip())
    data = [int(line.strip()) for line in lines[2:2+data_size]]

    return K, data_size, data


# --- Example Usage ---
if __name__ == "__main__":
    filename500k = "input_1mil.txt"
    filename1mil = "input_500k.txt"
    K, data_size, data = read_input(filename500k)
    J, data_size1, data1 = read_input(filename1mil)
    
    # Q1 analysis of data set 500k and 1mil
    q1starttime = time.time()
    dual_index = []  # This will store the indices of the two elements once found.
    dual_search(data, len(data), K, dual_index)
    q1endtime = time.time()
    q1_time_for_500k = q1endtime - q1starttime
    
    q1starttime = time.time()
    dual_index1 = []  # This will store the indices of the two elements once found.
    dual_search(data1, len(data1), K, dual_index1)
    q1endtime = time.time()
    q1_time_for_1mil = q1endtime - q1starttime
        
    # Q2 analysis of data set 500k and 1mil
    q2starttime = time.time()
    dual_index1 = []  # This will store the indices of the two elements once found.
    dual_sorted_search(data, len(data), K, dual_index)
    q2endtime = time.time()
    q2_time_for_500k = q2endtime - q2starttime
    
    q2starttime = time.time()
    dual_index1 = []  # This will store the indices of the two elements once found.
    dual_sorted_search(data1, len(data1), J, dual_index1)
    q2endtime = time.time()
    q2_time_for_1mil = q2endtime - q2starttime
    
    print()
    print("=" * 40)
    print("Analysis for Q1 for 500k and 1mil")
    print(f"Q1 : Search with bruteforce {q1_time_for_500k:.6f} seconds.")
    print(f"Q1 : Search with two pointers {q1_time_for_1mil:.6f} seconds.\n")
    
    print("Analysis for Q2 for 500k and 1mil")
    print(f"Q2 : Search with bruteforce {q2_time_for_500k:.6f} seconds.")
    print(f"Q2 : Search with two pointers {q2_time_for_1mil:.6f} seconds.\n")