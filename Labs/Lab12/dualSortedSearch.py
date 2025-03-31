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
            return True
        
        elif current_sum < K:
            left+=1
        elif current_sum > K:
            right-=1

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
    A = [9, 1, 4, 3, 7, 5]
    k = 8
    merge_sort(A)
    dual_index = []
    dual_sorted_search(A, len(A), k, dual_index)