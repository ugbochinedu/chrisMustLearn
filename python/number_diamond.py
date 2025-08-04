def number_diamond(n):
    for count in range(1, n + 1):
        print(' ' * (n - count), end='')
        for counter in range(1, count + 1):
            print(counter, end=' ')
        print()
   
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
number_diamond(5)