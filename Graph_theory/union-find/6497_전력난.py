# 6497 전력난
import sys
import heapq
sys.setrecursionlimit((10**5) * 2)

input = sys.stdin.readline

edge = []

def _union(a, b):
    a = _find(a)
    b = _find(b)
    if a == b:
        return False
    elif a < b:
        p[b] = a
    else:
        p[a] = b
    return True

def _find(i):
    if p[i] != i:
        p[i] = _find(p[i])
    return p[i]

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    p = [0] * (m + 1)
    for i in range(1, m + 1):
        p[i] = i
    save = 0
    total = 0
    for i in range(n):
        x, y, z = map(int, input().split())
        total += z
        heapq.heappush(edge, (z, x, y))
    while edge:
        cost, x, y = heapq.heappop(edge)
        if _union(x, y):
            save += cost
    print(total-save)

# 테스트 케이스가 여러번 주어지므로
# m, n을 입력받고 n 번동안 x,y,z 를 입력받음 -> 하나의 테스트 케이스
# 다시 처음으로 돌아가 m, n 이 0이라면 반복문 탈출