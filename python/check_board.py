size = 8
for count in range(size):
    for counter in range(size):
        if (count + counter) % 2 == 0:
            print("*", end="    ")
        else:
             print(" ", end=" ")
    print()