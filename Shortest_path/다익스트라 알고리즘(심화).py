import heapq

INF = int(10e9)

n,m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input())
graph = [[] for _ in range(n + 1)]
d = [INF] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (비용, 노드)의 튜플형태로 데이터 추가
    d[start] = 0
    while q:
        cost, dst = heapq.heappop(q) # 비용과 노드를 불러움
        if d[dst] < cost: # 큐에서 꺼내온 데이터가 거리정보 테이블에 저장된 값보다 크다면 데이터를 처리하지 않고 넘어간다.
            continue # 값이 같은 경우는 다른노드를 들려서 가면 비용이 증가할게 뻔하지만,, 처음 (0, start)의 케이스 땜에 등호는 빠진걸로 추측 
        # 꺼낸 것보다 테이블에 저장된 데이터가 더 최단거리일 땐 패스
        #         ㄴ> (Q. 힙에서 불필요한 데이터를 꺼내는건 시간복잡도에 큰 영향을 미치지 못하는가?)
        # 최단거리가 갱신될때마다 큐에 데이터를 추가하기 때문에, 같은 노드에 대한 거리정보가 여러개 담겨있을 수 있다. 테이블에 더 작은 값이 기록되어있다면 스킵
        # 노드를 방문하는 순간에 가장 최단 거리가 갱신되므로, 테이블에 담겨있는 값이 더 작다는 것은 그 노드가 이미 방문되었을 수도 있음.
        for _tuple in graph[dst]:
            sum_cost = cost + _tuple[1]
            if sum_cost < d[_tuple[0]]: # dst노드를 거쳐가는 경우가 더 짧은 거리일 때
                d[_tuple[0]] = sum_cost # 거리정보 테이블에 최단거리 갱신
                heapq.heappush(q, (sum_cost, _tuple[0])) # 큐에 (최단거리, 노드) 튜플 추가

dijkstra(start)

for i in range(1,n+1):
    if (d[i] == 0):
        print(i, "is start node")
    elif (d[i] != INF):
        print("node :",i,", distance :", d[i])
    else:
        print("node :", i, ", Can't visit")



'''
---입력값---
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

---출력값---
1 is start node
node : 2 , distance : 2
node : 3 , distance : 3
node : 4 , distance : 1
node : 5 , distance : 2
node : 6 , distance : 4

'''