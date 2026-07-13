N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

color = [0] * (N + 1)

Q = []  

s = 1
color[s] = 1
Q.append(s)

order = []

while Q:
    u = Q.pop(0) 
    order.append(u)
    for v in G[u]:
        if color[v] == 0:
            color[v] = 1
            Q.append(v)

print(*order)
