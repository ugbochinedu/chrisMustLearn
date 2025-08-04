def matrix_square(number):

    matrix = [[0] * number for _ in range(number)]

    num = 1
    top = 0
    bottom = number - 1
    left = 0
    right = number - 1
    

    while num <= number * number:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    
    for row in matrix:
        for num in row:
            print(f"{num:2d}", end=" ")
        print()
matrix_square(4)
