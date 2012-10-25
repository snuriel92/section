# Quicksort routine for given collection of elements.

# Simple version defined in wikipedia (uses O(n) memory)
def quicksort(elements):
    # If one or zero elements, then just return (technically already sorted)
    if (len(elements) <= 1):
        return elements
    else:
        # Choose pivot and then create lists containing elements that are
        # less than and greater than the pivot element.
        pivot = elements[len(elements) / 2]
        left = []
        right = []

        for i in range(len(elements)):
            if (i != len(elements)/2):
                if (elements[i] <= pivot):
                    left.append(elements[i])
                else:
                    right.append(elements[i])

        # Now just recursively call quicksort on the left & right lists and combine
        # at the end with the pivot element.
        return quicksort(left) + [pivot] + quicksort(right)

############################################################

# Mergesort
def mergesort(n):
    if len(n) > 1:
        mid = len(n) // 2
        a = n[mid:]
        b = n[:mid]
        if len(a) > 1:
            a = mergesort(a)
        if len(b) > 1:
            b = mergesort(b)
        return merge(a, b)
    else:
        return n 
   
def merge(a, b):
    result = []
    while a and b:
        if (a[0] < b[0]):
            result.append(a[0])
            a = a[1:]
        else:
            result.append(b[0])
            b = b[1:]
    if a:
        result.extend(a)
    else:
        result.extend(b)
    return result
    
############################################################
    
# (Modified code taken from http://codehost.wordpress.com/2011/07/22/radix-sort/)
# Radix sort for variable length strings
def radixsort(array):
    if (len(array) <= 1):
        return array
    maxLen = -1
    for string in array: # Find longest string
        strLen = len(string)
        if strLen > maxLen:
            maxLen = strLen
    oa = ord('!') - 1; # First character code
    oz = ord('~') - 1; # Last character code
    n = oz - oa + 2; # Number of buckets (+empty character)
    buckets = [[] for i in range(0, n)] # The buckets
    for position in reversed(range(0, maxLen)):
        for string in array:
            index = 0 # Assume "empty" character
            if position < len(string): # Might be within length
                index = ord(string[position]) - oa
            buckets[index].append(string) # Add to bucket
        del array[:]
        for bucket in buckets: # Reassemble array in new order
            array.extend(bucket)
            del bucket[:]
    return array

############################################################

# Selection sort algorithm
def selectionsort(arr):
    for i in range(0, len(arr)-1):
        minIndex = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr
