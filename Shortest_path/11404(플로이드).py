# 11404
import sys

input = sys.stdin.readline
INF = int(10e9)


n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n +1)]

for i in range(n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == INF:
        graph[a][b] = c
    elif graph[a][b] != INF and graph[a][b] > c:
        graph[a][b] = c

for visit in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][visit] + graph[visit][j] < graph[i][j]:
                graph[i][j] = graph[i][visit] + graph[visit][j]

for i in range(1, n+1):
    for j in range(1, n +1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()