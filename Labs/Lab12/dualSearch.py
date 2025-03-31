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
                return  # Exit as soon as a valid pair is found.
    
# --- Example Usage ---
if __name__ == "__main__":
    # Example input
    A = [3, 1, 7, 4, 5, 9]
    K = 8
    dual_index = []  # This will store the indices of the two elements once found.
    
    # Call the search function
    dual_search(A, len(A), K, dual_index)
    
    # Check if a pair was found and then print the result
    if dual_index:
        print(f"Pair found at indices: {dual_index}")
        print(f"Elements: {A[dual_index[0]]} + {A[dual_index[1]]} = {K}")
    else:
        print("No pair found that sums to", K)