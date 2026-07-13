n, m = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

adj_list = [[] for _ in range(n)]

for i in range(m):
    from_node = u[i] - 1  
    to_node = v[i]
    weight = w[i]
    adj_list[from_node].append((to_node, weight))


for i in range(n):
    edges = ' '.join(f"({des},{wt})" for des, wt in adj_list[i])
    print(f"{i + 1}: {edges}")
