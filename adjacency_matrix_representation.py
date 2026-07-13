n,m = map(int, input().split())
adj_mat =[]
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)

    adj_mat.append(row)
for k in range(m):
    u, v, w =map(int, input().split())
    adj_mat[u-1][v-1] = w
for row in adj_mat:
    print(' '.join(map(str, row))) 
