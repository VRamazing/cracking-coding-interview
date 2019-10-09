# Complexity - Best case, Avg case - nlogn,  Worst case - n*n
# Space - O(1)

import random

def mergeSort(Array):
    m = len(Array)//2

    if(len(Array)>1):
       
        l = Array[:m]
        r = Array[m:]

        mergeSort(l)
        mergeSort(r)

        i=0
        j=0
        k=0

        # newArray = [None for i in range(len(l)+len(r))]

        while(i < len(l) and j < len(r)):
            if(l[i]>r[j]):
                Array[k] = r[j]
                j+=1
            else:
                Array[k] = l[i]
                i+=1
            k+=1

        while(i < len(l)):
            Array[k] = l[i]
            i+=1
            k+=1

        if(j < len(r)):
            Array[k] = r[j]
            j+=1
            k+=1

        return Array

arrayToSort = [random.randint(0,10) for i in range(0,10)]
print("Array to sort", arrayToSort)
print("Sorted array", mergeSort(arrayToSort))