def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Iterate through each layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        # Iterate through each element in the current layer
        for i in range(first, last):
            offset = i - first
            
            # Store top element
            top = matrix[first][i]
            
            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top element to right
            matrix[i][last] = top
