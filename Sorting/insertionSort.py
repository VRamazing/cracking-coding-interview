# Complexity - Best case - n - Worst case - n*n
# Space - O(1)

import random

def insertionSort(Array):
    for i in range(1, len(Array)):
        for j in range(i, 0, -1):
            if (Array[j] < Array[j-1]):
                Array[j-1],Array[j] = Array[j],Array[j-1]
    return Array

arrayToSort = [random.randint(0,10) for i in range(0,10)]
print("Array to sort", arrayToSort)
print("Sorted array", insertionSort(arrayToSort))