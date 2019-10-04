def uniqueList(A):

    newList = []
    prevElem = A[0]
    lenOfList = len(A)
    for i in range(lenOfList-1):
      
        if(A[i] == A[i+1]):
            prevElem = A[i]
            
        else:
            newList.append(A[i])
           
    if(A[lenOfList-1]==A[lenOfList-2]):
         newList.append(A[lenOfList-1])
    return newList

print(uniqueList([1,2,2,3,3,3,4,5,6,6,6]))
