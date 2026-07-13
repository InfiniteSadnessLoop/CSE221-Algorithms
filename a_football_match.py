from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)
color = [-1] * (n + 1)
res = 0

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    color[start] = 0
    count = [1, 0] 

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                color[neighbor] = 1 - color[node]
                count[color[neighbor]] += 1
                visited[neighbor] = True
                queue.append(neighbor)
            elif color[neighbor] == color[node]:

                continue
    return max(count)

for i in range(1, n + 1):
    if not visited[i]:
        res += bfs(i)

print(res)
