# Complexity - Best case - n - Worst case - n*n
# Space - O(1)

import random

def bubbleSort(Array):
    for i in range(0, len(Array)):
        swapped = False
        for j in range(0, len(Array)-i-1):
            if (Array[j] > Array[j+1]):
                Array[j+1],Array[j] = Array[j],Array[j+1]
                swapped = True
        if(not swapped):
            break

    return Array

array = [random.randint(0,10) for i in range(0,10)]
print(bubbleSort(array))