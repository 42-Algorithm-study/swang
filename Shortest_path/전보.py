import heapq
   
INF = int(10e9) 
N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
d = [INF] * (N + 1)

# 간선입력 받아서 그래프에 저장
for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y,Z))

# 최소힙을 이용한 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while (q):
        cost, node = heapq.heappop(q)
        if (d[node] < cost):
            continue
        for _tuple in graph[start]:
            sum_cost = cost + _tuple[1]
            if (sum_cost < d[_tuple[0]]):
                d[_tuple[0]] = sum_cost
                
dijkstra(C)

# 연결이 닿는 도시 개수 : 총 도시 - INF 개수 + 1(0번노드는 없음) - 1(자기자신제외)
city_count = N - d.count(INF)
total_time = 0
# INF 제외 최대값 구하기
for i in d:
    if i != INF and total_time < i:
        total_time = i

# 연결이 닿는 도시와 최대 시간(동시에 전보를 치면 제일 오래걸리는 시간 출력)
print(city_count, total_time)

'''
input--
3 2 1
1 2 4
1 3 2

out---
2 4
'''