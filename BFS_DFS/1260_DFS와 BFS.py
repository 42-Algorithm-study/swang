from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
# print(graph)

# 주어지는 간선은 양방향이다
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# 작은 수의 노드부터 방문한다
for g in graph:
    g.sort()
#print(graph)


visit = [0] * (n + 1)
visit[0] = 1

def dfs(graph, visit, v):
    # 방문처리
    visit[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if visit[i] == 0:
            dfs(graph, visit, i)
            
def bfs(graph,visit, v):
    que = deque()
    que.append(v)
    visit[v] = 0
    visit[0] = 0
    while que:
        first = que.popleft()
        print(first, end=" ")
        for i in graph[first]:
            # visit이 dfs 수행으로 모두 1로 채워져있을 것( 반대로 조건문 생성)
            if visit[i] == 1:
                que.append(i)
                visit[i] = 0

dfs(graph, visit, v)
print()
bfs(graph, visit, v)

# 아무리 노드가 많아도 간선이 1개면 모든 노드를 방문 할 수 없음