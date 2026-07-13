from collections import deque

N, M, s, d = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

G = [[] for _ in range(N + 1)]
for i in range(M):
    u = u_list[i]
    v = v_list[i]
    G[u].append(v)
    G[v].append(u)

for neighbors in G:
    neighbors.sort()

color = [0] * (N + 1)
parent = [-1] * (N + 1)
Q = deque()

color[s] = 1
Q.append(s)
while Q:
    u = Q.popleft()
    if u == d:
        break
    for v in G[u]:
        if color[v] == 0:
            color[v] = 1
            parent[v] = u
            Q.append(v)

if parent[d] == -1 and s != d:
    print(-1)
else:
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(len(path) - 1)
    print(*path)
