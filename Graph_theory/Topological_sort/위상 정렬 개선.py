from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for i in range(n  + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

ret = []

def topology_sort(n):
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft() # 진입차수 0인 노드 추출
        ret.append(node) # 방문한 노드 담기
        for n in graph[node]: #진입차수가 0인 노드가 방문할 수 있는 노드들의 진입차수를 감소시켜줌
            indegree[n] -= 1
            if indegree[n] == 0: # 감소시킨 진입차수가 0일 경우 큐에 넣어줌
                q.append(n)

topology_sort(n)

print(ret)