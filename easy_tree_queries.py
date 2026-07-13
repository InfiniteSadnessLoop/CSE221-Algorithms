import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)
 
n, r = map(int, input().split())
g = [[] for _ in range(n + 1)]
 
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
 
sz = [0] * (n + 1)
 
def dfs(u, par):
    sz[u] = 1
    for v in g[u]:
        if v != par:
            dfs(v, u)
            sz[u] += sz[v]
 
dfs(r, 0)
 
q = int(input())
for _ in range(q):
    print(sz[int(input())])
