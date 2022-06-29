# 2. DFS 탐색 구현 (스택 대신 재귀로)
def DFS(now, graph, visit):
	visit[now] = 1
	if 0 not in visit:
		print(now)
		return
	print(now, end=" -> ")
	for i in graph[now]:
		if visit[i] == 0:
			DFS(i, graph, visit)
	return


# 1. 그래프를 인접행렬로 구현
graph = [
	[],
	[2, 8, 3],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

# 방문처리용
visit = [0] * 9
visit[0] = 2
# 1번부터 탐색 시작
DFS(1, graph, visit)