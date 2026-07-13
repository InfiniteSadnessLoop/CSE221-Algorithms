def find_moves(n, start_x, start_y):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), 
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    valid_moves = []

    for x, y in directions:
        new_x, new_y = start_x + x, start_y + y
        if 1 <= new_x <= n and 1 <= new_y <= n:
            valid_moves.append((new_x, new_y))

    valid_moves.sort() 
    return valid_moves

n = int(input())
x, y = map(int, input().split())

moves = find_moves(n, x, y)
print(len(moves))
print('\n'.join(f"{a} {b}" for a, b in moves))
