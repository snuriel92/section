# Provides the merge sort algorithm with the following set of performance 
# characteristics
#     best    -- O(n log n) 
#     average -- O(n log n) 
#     worst   -- O(n log n) 
# This implementation does not sort in place. Instead, it returns a new 
# instance of the sorted array. 
# 
# We might also want to consider using the .sort function in Python which
# to the best of my understanding it is base on Timsort.
# Performance characteristics for Timsort are clearly described at :
#    https://secure.wikimedia.org/wikipedia/en/wiki/Timsort
# 

def sort(array):
    if len(array) <= 1:
        return array
    else:
        left  = array[:len(array)/2] 
        right = array[len(array)/2:] 
        return merge(sort(left),sort(right))

def merge(array1, array2):
    merged_array = []
    p1, p2 = 0, 0
    
    while p1 < len(array1) and p2 < len(array2):
        if array1[p1] < array2[p2]:
            merged_array.append(array1[p1])
            p1 += 1
        else:
            merged_array.append(array2[p2])
            p2 += 1
            
    while p1 < len(array1):
        merged_array.append(array1[p1])
        p1 += 1

    while p2 < len(array2):
        merged_array.append(array2[p2])
        p2 += 1

    return merged_array
