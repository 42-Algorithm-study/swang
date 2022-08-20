from collections import deque

n, m = map(int, input().split())

indegree = [0 * (n + 1)]
q = deque()
graph = [[] for i in range(n  + 1)]

for i in range(m):
    a, b = map(int, input().split()) #a에서 b로가는 방향 간산이 존재한다
    # print(a, b)
    graph[a].append(b)
    indegree[b] += 1

ret = []

def find_indegree():
    for i in range(1, n + 1):
        if indegree[i] == 0:
            indegree[i] -= 1
            q.append(i)

find_indegree()

while q:
    node = q.popleft()
    ret.append(node)
    for n in graph[node]:
        indegree[n] -= 1
    if len(q) == 0:
        find_indegree()

print(ret)