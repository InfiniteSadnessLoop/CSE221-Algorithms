from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])
    farthest_node = start

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > visited[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, visited[farthest_node]

node_a, l = bfs(1)

node_b, diameter = bfs(node_a)

print(diameter)
print(node_a, node_b)
