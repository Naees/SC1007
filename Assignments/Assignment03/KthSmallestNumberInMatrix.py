"""
Question 7
Max score: 100
The Kth smallest number in a sorted matrix (row and column-wise sorted)

Given an n by n matrix (2D array) where each row and column is sorted in non-decreasing order, find the k-th smallest element. For example, given the 3 by 3 matrix

1 5 9
10 11 13
12 13 15

The 5th smallest number is 11. The 7th and 8th smallest numbers are both 13.

The method header is:

kth_smallest_linear (matrix, k) :

For example, for the input
3 5
1 5 9
10 11 13
12 13 15

where the first line contains two integers n (l.e., the number of columns and rows) and k. Each of the next n lines contains n integers (each line represents a row).
The output will be 11."""

def kth_smallest(matrix, k):
    #insert your codes here
    n = len(matrix)
    # The smallest element is located at the top-left and the largest at the bottom-right.
    low, high = matrix[0][0], matrix[n - 1][n - 1]
    
    # Binary search on the range of possible values.
    while low < high:
        mid = (low + high) // 2  # Candidate value to check.
        count = 0 # To count how many elements are <= mid.
        
        # Perform a "staircase" traversal from the top-right corner.
        # This loop efficiently counts all elements in the matrix less than or equal to mid.
        row, col = 0, n - 1
        while row < n and col >= 0:
            if matrix[row][col] <= mid:
                # If matrix[row][col] is <= mid, then all elements in this row up to col are <= mid.
                count += col + 1
                row += 1  # Move down to the next row.
            else:
                col -= 1  # Move left in the current row to find a smaller element.
        
        # Adjust the binary search boundaries based on the count.
        if count < k:
            # There are fewer than k elements <= mid, so the kth smallest must be > mid.
            low = mid + 1
        else:
            # Otherwise, the kth smallest is mid or smaller.
            high = mid
    
    # When the search narrows down to a single value, low (or high) is the kth smallest element.
    return low
        
        

#read the input
n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
#output
print(kth_smallest(matrix, k))

"""
Sample input:
3 5
1 5 9
10 11 13
12 13 15

Sample output:
11
"""