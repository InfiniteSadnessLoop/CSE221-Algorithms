import math

def build_graph(n):

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):  
            if math.gcd(i, j) == 1:
                graph[i].append(j)
                graph[j].append(i) 
    
    for k in range(1, n + 1):
        graph[k].sort()
    return graph

def process_queries(graph, q):

    for _ in range(q):
        x, y = map(int, input().split())
        if y > len(graph[x]):
            print("-1")
        else:
            print(graph[x][y - 1])

n, q = map(int, input().split())

graph = build_graph(n)

process_queries(graph, q)
