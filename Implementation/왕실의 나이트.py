# 4.구현
# 2) 왕실의 나이트

where = input()
row = where[1]
col = where[0]

# 두칸 갈 수 있는지 체크
# (초기 위치에서 4방향으로 뻗어 나갈 수 있는지)
U, D, L, R = 0, 0, 0, 0
# 각 방향으로 두칸씩 전진 후 수직/수평으로 한칸 갈 수 있는지 체크
u, d, l, r = 0, 0, 0, 0

# 각 방향 조건에 따라서 대문자, 소문자 on/off 설정
if (row > '2'):
    U = 1
    u = 1
elif (row == '2'):
    u = 1

if (row < '7'):
    D = 1
    d = 1
elif (row == '7'):
    d = 1

if (col > 'b'):
    L = 1
    l = 1
elif (col == 'b'):
    l = 1

if (col < 'g'):
    R = 1
    r = 1
elif (col == 'g'):
    r = 1
    
# print(U,D,L,R )
# print(u,d,l,r)

ret = 0

# 각 방향으로 갈 수 있으면 1 * (수평/수직으로 한 칸 갈 수 있는지 여부)
# 각 방향으로 갈 수 없다면 0 * (수평/수직으로 한 칸 갈 수 있는지 여부)
ret += D * (l + r)
ret += U * (l + r)
ret += L * (u + d)
ret += R * (u + d)

print(ret)

# 테스트 케이스
# a1 (2)
# h7 (3)
# c2 (6)
# f4 (8)
