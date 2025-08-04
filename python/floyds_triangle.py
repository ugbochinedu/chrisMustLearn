def floyds_triangle(rows):
    num = 1
    for i in range(rows):
        row = ''
        for j in range(i + 1):
            row += str(num) + ' '
            num += 1
        print(row)

floyds_triangle(5)