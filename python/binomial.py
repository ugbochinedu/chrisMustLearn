def binomial(n, k):
    count = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        count = count * (n - i)
        count = count // (i + 1)
    return count

rows = 6
for i in range(rows + 1):
    for j in range(i + 1):
        print(binomial(i, j), end=" ")
    print()