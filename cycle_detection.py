import sys
sys.setrecursionlimit(2 * 100000 + 5)

def has_cycle(u, graph, color):
    color[u] = 'G' 
    for v in graph[u]:
        if color[v] == 'W': 
            if has_cycle(v, graph, color):
                return True
        elif color[v] == 'G': 
            return True
    color[u] = 'B' 
    return False

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

color = ['W'] * (N + 1)

for node in range(1, N + 1):
    if color[node] == 'W':
        if has_cycle(node, graph, color):
            print("YES")
            break
else:
    print("NO")
