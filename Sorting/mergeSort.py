# Complexity - Best case, Avg case - nlogn,  Worst case - n*n
# Space - O(1)

import random

def mergeSort(Array):
    m = len(Array)//2

    if(m==0):
        return
    
    l = Array[:m]
    r = Array[m:]

    mergeSort(l)
    mergeSort(r)

    i=0
    j=0
    k=0

    newArray = [None for i in range(len(l)+len(r))]

    while(i < len(l) and j < len(r)):
        if(Array[i]>=Array[j]):
            newArray[k] = Array[j]
            j+=1
        else:
            newArray[k] = Array[i]
            i+=1
        k+=1

    if(i < len(l)):
        newArray[k] = Array[j]

    if(j < len(r)):
        newArray[k] = Array[i]

    print(newArray)
    return newArray

arrayToSort = [random.randint(0,10) for i in range(0,10)]
print("Array to sort", arrayToSort)
print("Sorted array", mergeSort(arrayToSort))