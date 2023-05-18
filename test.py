l = list(map(int, input().split()))
res = {}
for i in range(len(l) ):
    res[l[i]] = res[res[l[i + 1]]]
print(res)
