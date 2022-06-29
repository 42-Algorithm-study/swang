n, m = map(int, input().split())

t = []
# 얼음틀 입력받기
for i in range(n):
	t.append(list(map(int, input())))

# 얼음틀 출력
# print(t)

# 얼음틀 인접 칸 탐색 함수
# 맵을 이동하면서 0인부분을 2로 바꾸며 탐색
# 좌표가 0인 인접노드를 모두 방문 했다면 덩어리 1개
def dfs(now_n, now_m, t):
	t[now_n][now_m] = 2
	# 오른쪽으로 탐색
	if (now_m < m - 1 and t[now_n][now_m + 1] == 0):
		dfs(now_n, now_m+1 ,t)
	# 왼쪽으로 탐색
	if (now_m > 0 and t[now_n][now_m - 1] == 0):
		dfs(now_n, now_m - 1, t)
	# 아래로 탐색
	if (now_n < n - 1 and t[now_n + 1][now_m] == 0):
		dfs(now_n +1, now_m, t)
	# 위로 탐색
	if (now_n > 0 and t[now_n -1][now_m] == 0):
		dfs(now_n -1, now_m, t)
	return 1

# 탐색 시작
# 모든 맵에 0이 없으면 탐색종료
ret = 0
for i in range(n):
	for j in range(m):
		if (t[i][j] == 0):
			ret += dfs(i, j, t)
# print(t)
print(ret)