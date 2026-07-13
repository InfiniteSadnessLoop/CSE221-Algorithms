N = int(input())
adj_matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    inp = list(map(int, input().split()))
    k = inp[0]
    adj = inp[1:]
    for j in adj:
        adj_matrix[i][j] = 1

for row in adj_matrix:
    print(' '.join(map(str, row)))
