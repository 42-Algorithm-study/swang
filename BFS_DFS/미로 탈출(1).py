from collections import deque

n, m = map(int, input().split())

mapp = []
for i in range(n):
	mapp.append(list(map(int, input())))

# 상 하 좌 우
dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

que = deque()
que.append((0,0))

while que:
	x, y = que.popleft()
	for i in range(4):
		nx = x + dn[i]
		my = y + dm[i]
		if (nx >= n or nx < 0 or my >= m or my < 0):
			continue
		if mapp[nx][my] == 0:
			continue
		if mapp[nx][my] == 1:
			mapp[nx][my] = mapp[x][y] + 1
			que.append((nx,my))

print(mapp[n-1][m-1])
