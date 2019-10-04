def zeroAtMatrix(A_copy):
	A=A_copy
	rows = len(A)
	cols = len(A[0])
	stop = False
	zeroList = []

	#searching position for element with value zero
	for row in range(rows):
		for col in range(cols):
			if(A[row][col]==0):
				stop = True
				zeroList.append((row, col))

	#zeroing on element value
	for pos in zeroList:
		i=0
		j=0

		while(j<cols):
			A[pos[0]][j]=0
			j+=1
		while(i<rows):
			A[i][pos[1]]=0
			i+=1

	print(A_copy)

multiList = [[1,2,3],[2,0,5],[5,6,0]]
newList = multiList.copy()
# print(multiList)

zeroAtMatrix(newList)

print(multiList)

#Time complexity n2