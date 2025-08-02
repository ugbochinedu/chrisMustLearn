def print_inverted_pyramid(rows):
    for count in range(rows, 0, -1):
        print(' ' * (rows - count) + '* ' * count)


  