from collections import deque

n, m = map(int, input().split())

_map = []
for i in range(n):
	_map.append(list(map(int, input())))

que = deque()
# 좌표는 1,1 이지만 인덱스 값은 0,0 부터 시작
que.append((0,0))

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while _map[n-1][m-1] == 1: # n,m 은 4보다 같거나 큼, 1이 아니면 탈출하도록 설정
	x, y = que.popleft()
	for i in range(4):
		new_x = x + dx[i]
		new_y = y + dy[i]
		# 인덱스 범위값 벗어나는 경우 스킵
		if (new_x < 0 or new_y < 0 or new_x >= n or new_y >= m):
			continue
		if (_map[new_x][new_y] == 0):
			continue
		# 맵의 값이 1이라면 처음 방문 노드 재방문이라면 거리값이 들어있을 것
		# (첫번째 출발칸을 다시 밟는다해도 어차피 우리는 오른쪽 하단 값만 확인하면 된다)
		if (_map[new_x][new_y] == 1):
			# 지금 노드의 거리 값보다 1 증가한 값을 넣어줌
			_map[new_x][new_y] = _map[x][y] + 1
			# 처음 방문하는 노드들을 대기열에 넣어줌
			que.append((new_x, new_y))

print(_map[n-1][m-1])