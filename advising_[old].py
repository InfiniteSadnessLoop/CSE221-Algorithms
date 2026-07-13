from collections import deque
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indeg[b] += 1

queue = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        queue.append(i)

res = []
while queue:
    node = queue.popleft()
    res.append(node)
    for neighbor in adj[node]:
        indeg[neighbor] -= 1
        if indeg[neighbor] == 0:
            queue.append(neighbor)

if len(res) == n:
    print(' '.join(map(str, res)))
else:
    print(-1)
