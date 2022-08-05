# 1753
import heapq
import sys
input = sys.stdin.readline

INF = int(10e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
d = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if (d[node] < cost):
            continue
        for _tuple in graph[node]:
            sum_cost = cost + _tuple[1]
            if (d[_tuple[0]] > sum_cost):
                d[_tuple[0]] = sum_cost
                heapq.heappush(q, (sum_cost, _tuple[0]))

dijkstra(K)

# print(d)

for i in range(1, len(d)):
    if (d[i] == INF):
        print("INF")
    else:
        print(d[i])
        
'''
input---
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

out-----
0
2
3
7
INF
'''
