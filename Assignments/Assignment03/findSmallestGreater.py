"""Question 6
Max. score: 100
Find the smallest number greater than the target
You are given a sorted list of integers (no duplicates) and a target number. Your task is to find the smallest number in the list that is greater than the target.
If such a number does not exist, return -1.

The method header is:

def find_smallest_greater(arr, x) :
where the first line indicates two integers n and x - the number of elements and the target, and the second line contains n sorted integers.

The output will be -1.
Consider using the binary-search based algorithm. The brute-force algorithm will report "Time limit exceeded" error for some test cases."""

def find_smallest_greater(arr, x):
    #insert your codes here
    startIndex = 0
    endIndex = len(arr)

    while startIndex <= endIndex:
        mid = (startIndex + endIndex) // 2

        # If the mid element is x
        if arr[mid] == x:
            startIndex = mid + 1

        # If the mid element is greater than x
        elif arr[mid] > x:
            endIndex = mid

        # If the mid element is lower than x
        elif arr[mid] < x:
            startIndex = mid + 1

    return arr[startIndex] if startIndex < len(arr) else -1

#read input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(find_smallest_greater(arr, x))

"""
Sample Test Case:
5 9
1 2 3 4 5

Sample output:
-1
"""