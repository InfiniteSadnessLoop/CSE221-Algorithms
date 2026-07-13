from collections import deque

def bfs(start, target, graph, N):
    visited = [False] * (N + 1)
    parent = [-1] * (N + 1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        u = q.popleft()
        if u == target:
            break
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    if not visited[target]:
        return None
    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path
N, M, S, D, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
path1 = bfs(S, K, graph, N)
path2 = bfs(K, D, graph, N)

if path1 is None or path2 is None:
    print(-1)
else:
    full_path = path1 + path2[1:]
    print(len(full_path) - 1)
    print(*full_path)
