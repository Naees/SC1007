"""Question 8
Max. score: 100.00

First occurrence in a sorted array

You're given a sorted array of integers (possibly with duplicates). Write a function to find the index of the first occurrence of a given target number. If the target is not present, return -1.

The method header is:
def first_occurrence(arr, target) :

where art is the sorted array given, and target is the number we are looking for.
For example, for the input:

6 2
1 2 2 2 3 4

where the first line indicates two integers n (size of array) and x (target value), and the second line contains space-separated integers (sorted in non-decreasing order).
The output will be 1.

Consider using binary-search based algorithm. Brute-force algorithm will report "Time limit exceeded" for some test cases."""

def first_occurrence(arr, target):
    #insert your codes
    startIndex = 0
    endIndex = len(arr)
    first_index = -1 

    while startIndex < endIndex:
        mid = (startIndex + endIndex) // 2

        # mid is target
        if arr[mid] == target:
            # take note of this occurence and continue the loop
            # this continuation allows you to find earlier iterations of a target if it exist
            first_index = mid
            endIndex = mid - 1

        # mid smaller than target
        elif arr[mid] < target:
            startIndex = mid + 1

        # mid larger than target
        elif arr[mid] > target:
            endIndex = mid
    
    if first_index == -1:
        return -1
    
    return first_index

n, target = map(int, input().split())
arr = list(map(int, input().split()))
result = first_occurrence(arr, target)
print(result)

"""
Sample input:
6 2
1 2 2 2 3 4

Sample output:
1
"""