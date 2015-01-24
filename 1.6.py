def rotate(matrix, n):
	for layer in range(n/2):
		first = layer
		last = n - layer - 1
		for index in range(n):
			top = matrix[first][index]
			matrix[first][i] = matrix[last - index][index]

