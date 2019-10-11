# Complexity - Best case, Avg case - nlogn,  Worst case - n*n
# Space - O(1)

import random

def quickSort(Array):
    pivot = Array[0]
    lengthArray = len(Array)
    i=1
    j=lengthArray - 1

    while(j > i):

        while(pivot < Array[i]):
            i+=1

        while(pivot > Array[i]):
            j+=1

        Array[i], Array[j] = Array[j], Array[i]

    Array[0], Array[i] = Array[i], Array[0]

    return Array

arrayToSort = [random.randint(0,10) for i in range(0,10)]
print("Array to sort", arrayToSort)
print("Sorted array", quickSort(arrayToSort))