def inverted_pyramid(rows):
    for count in range(rows, 0, -1):
        print(' ' * (rows - count) + '* ' * count)

inverted_pyramid(5)
  