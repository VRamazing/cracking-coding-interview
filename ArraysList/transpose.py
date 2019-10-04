def transpose(Arr):
    rows = len(Arr)
    cols = len(Arr[0])
    boolChecker = [[False for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            Arr[i][j],Arr[j][i] = Arr[j][i], Arr[i][j]

            if(boolChecker[i][j]==False or boolChecker[j][i]==False):
                Arr[i][j],Arr[j][i] = Arr[j][i], Arr[i][j]
                boolChecker[i][j] = True
                boolChecker[j][i] = True
            else:
                continue

    print(Arr)

transpose([[1,2,3],[4,5,6],[7,8,9]])