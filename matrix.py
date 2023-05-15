n = int(input())
l = [[0 for _ in range(n)] for _ in range(n)]
a, b, c = map(int, input().split())
for i in range(n):
    for j in range(n):
        if i == j:
            l[i][j] = c
        elif i > j:
            l[i][j] = b
        else:
            l[i][j] = a
for i in range(n):
    print(*l[i])
