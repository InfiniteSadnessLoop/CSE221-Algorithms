from collections import deque

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False] * H for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    diamonds = 1 if grid[start_r][start_c] == 'D' else 0

    while queue:
        x, y = queue.popleft()
        for dr, dc in directions:
            nx, ny = x + dr, y + dc
            if 0 <= nx < R and 0 <= ny < H:
                if not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    if grid[nx][ny] == 'D':
                        diamonds += 1
    return diamonds

max_diamonds = 0

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            max_diamonds = max(max_diamonds, bfs(i, j))

print(max_diamonds)
