# Complexity -  All case - n*n
# Space - O(1)

import random

def selectionSort(Array):
    for i in range(0, len(Array)):
        for j in range(i+1, len(Array)):
            if (Array[i] > Array[j]):
                Array[i],Array[j] = Array[j],Array[i]


    return Array

array = [random.randint(0,10) for i in range(0,10)]
print(selectionSort(array))