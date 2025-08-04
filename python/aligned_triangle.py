size = 5
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end=" ")
    for k in range(i):
        print(k + 1, end=" ")
    print()
