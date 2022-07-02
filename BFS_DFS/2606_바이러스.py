n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
visit[0] = 2

def dfs(now, graph, visit):
    visit[now] = 1
    for g in graph[now]:
        if visit[g] == 0:
            dfs(g, graph, visit)
dfs(1, graph, visit)
# "1번 컴퓨터로부터" 감염된 컴퓨터 수
print(visit.count(1) - 1)