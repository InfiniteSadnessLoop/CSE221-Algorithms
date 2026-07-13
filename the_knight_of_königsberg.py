from collections import deque

def knight_moves(N, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0

    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    visited = [False] * ((N + 1) * (N + 1))

    def get_index(x, y):
        return x * (N + 1) + y

    queue = deque()
    queue.append((x1, y1))
    visited[get_index(x1, y1)] = True

    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if x == x2 and y == y2:
                return steps

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 1 <= nx <= N and 1 <= ny <= N:
                    idx = get_index(nx, ny)
                    if not visited[idx]:
                        visited[idx] = True
                        queue.append((nx, ny))
        steps += 1

    return -1

N = int(input())
x1, y1, x2, y2 = map(int, input().split())
print(knight_moves(N, x1, y1, x2, y2))
