def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to optimize the algorithm if the array is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, then the array is sorted
        if not swapped:
            break
    
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
