INF = int(10e9)

n, m = map(int, input().split()) #노드와 간선의 개수
start = int(input())
graph = [[] for _ in range(n + 1)] #튜플 활용예정
visit = [False] * (n+1) # 방문여부 체크용
d = [INF] * (n + 1) # 거리테이블 무한으로 초기화

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))

def get_cheep_node():
    _min = INF
    _cheep = 0
    for i in range(1, n+1):
        if d[i] < _min and visit[i] == False: #방문한적없고 최소값보다 작다면 
            _min = d[i]
            _cheep = i
    return _cheep # 제일 비용이 싼 노드의 인덱스를 반환함
    
def dijkstra(start):
    d[start] = 0 # 자기자신으로 가는 비용은 0
    visit[start] = True
    for _tuple in graph[start]: # start노드와 연결된 정보 불러오기
        d[_tuple[0]] = _tuple[1]
    for _ in range(n - 1): # 시작노드를 제외한 개수만큼 반복하면 됨 
        cheep = get_cheep_node()
        visit[cheep] = True
        # cheep을 거쳐서 가는 최단거리 갱신
        for _tuple in graph[cheep]:
            if d[_tuple[0]] > d[cheep] + _tuple[1]: # cheep 들려서 가는게 더 저렴하면
                d[_tuple[0]] = d[cheep] + _tuple[1] # 그 값으로 바꿔줌 | _tuple[0] 은 목적지 _tuple[1] 은 비용
dijkstra(start)

# print("v", visit)
# print("d", d)

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