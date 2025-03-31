def find_median_sorted_arrays(num1, num2):
    """
    #num1 (list): First sorted array.
    # num2 (list): Second sorted array.
    # Returns:
    # float: The median of the combined sorted array.
    """
    total_len = len(num1) + len(num2)
    # When theres an even number of elements
    # Return average of two middle elements
    if total_len % 2 == 0:
        return (find_kth_value(total_len//2, num1, num2) +
                find_kth_value(total_len//2)-1, num1, num2)
    # When theres an odd number of elements
    # Return the find Kth element
    return find_kth_value(total_len//2, num1, num2)

    
def find_kth_value(k, num1, num2):
    if len(num1) == 0:
        return num2[k]
    if len(num2) == 0:
        return num1[k]

    mid1 = len(num1) // 2
    mid2 = len(num2) // 2
    
    
    # We can tell if k is on the right side of the array of the left side
    # This condition tells us that k is on the right side (as the value will be greater than the sum of the two mid elements of both arrays) 
    if k > mid1+mid2:
        if num1[mid1] > num2[mid2]:
            # As K is on the right we eliminate the left half of the two arrays and 
            # update K by substracting the numebr of elements we have eliminated
            return find_kth_value(k-mid2-1, num1, num2[mid2+1:])
        # If the middle element of numbs2 is larger we eliminate the left half of the numbs one
        else:
            return find_kth_value(k-mid1-1, num1[mid1+1:], num2)
    # If K on the left side
    else:
        # If the middle element of nums one is larger
        if num1[mid1] > num2[mid2]:
        # Elimated the right half of the num1
            return find_kth_value(k, num1[:mid1], num2) # We don't have to update K as we are removing from the end rather tha n from the front
        # If the middle element of num2 is larger 
        else:
            # Elimate the right half of num2
            return find_kth_value(k, num1, num2[:mid2])
        

if __name__ == "__main__":
    num1 = [1, 3, 8]
    num2 = [7, 9, 10, 11]
    print(f"Median of the two sorted arrays is : {find_median_sorted_arrays(num1, num2)}")
