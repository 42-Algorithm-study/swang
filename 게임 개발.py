# a[x][y]가 갈 수 있는 칸 인지 체크
def check_go_tile(x,y,a):
    if (a[x][y] == '1' or a[x][y] == '2'):
        return 0
    else:
        return 1

# 현재 위치에서 갈 수 있는 길이 없는지 체크
def check_new_tile(x, y, a):
    ret = 0
    ret += check_go_tile(x-1, y, a)
    ret += check_go_tile(x, y-1, a)
    ret += check_go_tile(x+1, y, a)
    ret += check_go_tile(x, y+1, a)
    if (ret == 0):
        return False
    else:
        return True

# 뒤가 바다인지 체크
def check_back_sea(x, y, a):
    if (a[x][y] == '1'):
        return True
    else:
        return False
        
n, m = map(int, input().split())
r, c, d = map(int, input().split())

a = list()
for i in range(n):
    a.append(input().split())

# 북0 동1 남2 서3 인덱스를 참조하여 좌표 값에 더하면 칸을 이동할 수 있다
dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]

# 처음 시작한 칸 방문처리
a[r][c] = '2'
count = 1
print("check_tile:", count)

while True:
	# ---------게임 시작-----------
	print()
	print("-------start-------")
	print("diretion :" , d)
	# 4방향 중 새로 갈 타일이 없다면?
	if (check_new_tile(r,c,a) == False):
		print("❌ no new tile")
		# 바라보고 있는 방향의 뒷 칸이 바다라면?
		if (check_back_sea(r - dn[d], c - dm[d], a) == True):
			print("❌ noway")
			break
		else:
			# 바다가 아니라면 뒤로 한칸
			print("🔙 go back")
			r -= dn[d]
			c -= dm[d]
			print("go to start")
			# 다시 처음으로...
			continue
	# 새로 방문 할 타일이 존재한다면
	else:
		print("🔄 rotate:", d, end="")
		# 왼쪽으로 회전..  북0 서3 남2 동1 이므로
		# 방향 인덱스를 -1, 0일경우 3
		if (d == 0):
			d = 3
		else:
			d -= 1
		print(" ->", d)
	# 얖이 방문하지 않은 칸이라면,,, 한칸전진
	if (check_go_tile(r + dn[d], c + dm[d], a) == 1):
		# r,c좌표 수정
		r += dn[d]
		c += dm[d]
		print("✅ check way", d, "tile:", a[r][c])
		# 새로 방문하는 칸이라면?...
		if (a[r][c] != '2'):
			a[r][c] = '2'
			# 방문한 칸 수++
			count += 1
			print("check tile: ", count)
print()
print("all visit tile:", count)