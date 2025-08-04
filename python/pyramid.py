def pyramid(rows):
    for count in range(rows):
        print(' ' * (rows - count - 1) + '* ' * (count + 1))

pyramid(5)