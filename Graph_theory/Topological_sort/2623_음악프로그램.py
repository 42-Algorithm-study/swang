# 위상정렬에서 사이클이 발생하는 경우는 에러처리하기
from collections import deque

N, M = map(int, input().split())
p = [i for i in range(N + 1)]

graph = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)

for _ in range(M):
    lst = list(map(int, input().split()))
    for i in range(1, lst[0]):
        graph[lst[i]].append(lst[i + 1])
        indegree[lst[i + 1]] += 1

def topology_sort():
    q = deque()
    ret = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        singer = q.popleft()
        ret.append(singer)
        for _next in graph[singer]:
            indegree[_next] -= 1
            if indegree[_next] == 0:
                q.append(_next)
    if len(ret) != N: # 사이클이 발생하면... ret리스트의 길이가 N개가 안됨...
      print(0)        #(모든 노드를 방문하지 않아도 진입차수가 0인 노드가 없어지면 종료됨)
                      # 순서를 정할 수 없을 땐 0을 출력
    else:
        for s in ret:
            print(s)

topology_sort()