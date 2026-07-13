N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

indeg = [0] * (N + 1)
outdeg = [0] * (N + 1)

for i in range(M):
    outdeg[u[i]] += 1
    indeg[v[i]] += 1
output = [] 
for i in range(1, N + 1):
    output.append(indeg[i] - outdeg[i])
print(*output)
