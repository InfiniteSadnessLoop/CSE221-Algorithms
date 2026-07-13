N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

degree = [0] * (N + 1)
for i in range(M):
    degree[u[i]] += 1
    degree[v[i]] += 1

count = 0
for d in degree:
    if d % 2 == 1:
        count += 1

if count == 0 or count == 2:
    print("YES")
else:
    print("NO")
