import sys
sys.setrecursionlimit(2*100000+5)

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

G = [[] for _ in range(n + 1)]
for i in range(m):
    G[u[i]].append(v[i])
    G[v[i]].append(u[i])  

for adj in G:
    adj.sort()

colour = [0] * (n + 1) 
result = []

def DFS(G, u):
    colour[u] = 1
    result.append(u)
    for v in G[u]:
        if colour[v] == 0:
            DFS(G, v)

DFS(G, 1)
print(' '.join(map(str, result)))
