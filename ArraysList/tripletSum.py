
#n3 complexity
def tripletWithSum(A, sum):
    arr_size = len(A)
    for i in range(0, arr_size-2):
        for j in range(i+1, arr_size-1):
            for k in range(j+1, arr_size):
                if(A[i]+A[j]+A[k] == sum):
                    print("Triplet is", A[i],",",A[j],",",A[k])
                    return True
    return False


#nlogn complexity
def tripletWithSum2(A, sum):
    A.sort()
    arr_size=len(A)
    for i in range(0, arr_size-2):
        l=i+1
        r=arr_size-1
        while(l<r):
            if(A[i]+A[l]+A[r] == sum):
                print("Triplet is", A[i],",",A[l],",",A[r])
                return True
            elif(A[i]+A[l]+A[r] < sum):
                l += 1
            else:
                r -= 1



# Python3 program to find a triplet using Hashing 
# returns true if there is triplet with sum equal 
# to 'sum' present in A[]. Also, prints the triplet 
def tripletWithSum3(A, sum):
    arr_size = len(A)
    for i in range(0, arr_size-1): 
        # Find pair in subarray A[i + 1..n-1]  
        # with sum equal to sum - A[i] 
        s = set() 
        curr_sum = sum - A[i] 
        for j in range(i + 1, arr_size): 
            if (curr_sum - A[j]) in s: 
                print("Triplet is", A[i],  
                        ", ", A[j], ", ", curr_sum-A[j]) 
                return True
            print(A[j])
            s.add(A[j]) 
      
    return False

print(tripletWithSum3([1,3,45,6,10,8], 24))