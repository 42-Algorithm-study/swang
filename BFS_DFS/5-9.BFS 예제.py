# DFS 예제와 똑같은 그래프임

from collections import deque

graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
]

visit = [0] * 9
visit[0] = 1
que = deque()
# 처음 시작노드 1을 큐에 추가
que.append(1)
while True:
	# 방문하지 않은 노드가 없으면 반복문 탈출
	if 0 not in visit:
		break
	# 큐(대기열)의 첫번째 노드를 방문처리 && 출력
	first = que[0]
	visit[first] = 1
	print(que.popleft(), end=" -> ")
	#첫번째 노드의 인접 노드중 방문하지 않은 노드를 큐에 담고 방문처리
	for i in graph[first]:
		if visit[i] == 0:
			que.append(i)
			visit[i] = 1

# 큐에 남은 노드들을 출력 (마지막 노드는 화살표 안붙임)
for i in range(len(que)):
	if (len(que) == 1):
		print(que.popleft())
	else:
		print(que.popleft(), end=" -> ")
	