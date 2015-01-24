
def matrixSet(M, N, matrix):
	setrow = []
	setline = []
	for row in range(M):
		flag = 0
		for line in range(N):
			if matrix[row][line] == 0:
				flag = 1
				print line
				setline.append(line)
		if flag == 1:
			setrow.append(row)
	for line in range(N):
		for eachrow in setrow:
			matrix[eachrow][line] = 0
	for row in range(M):
		for eachline in setline:
			matrix[row][eachline] = 0
	return matrix

matrix = [[1 for x in range(5)] for x in range(5)]
matrix[0][2] = 0
matrix[1][3] = 0
matrix[2][4] = 0
print matrixSet(5,5,matrix)

