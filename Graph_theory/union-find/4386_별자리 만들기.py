import heapq
import sys
import math

input = sys.stdin.readline
n = int(input())
star = [[] for _ in range(n + 1)]
total = 0
edge = []
p = [0] * (n + 1)
for i in range(n + 1):
    p[i] = i

for i in range(1, n + 1):
    x, y = map(float, input().split())
    star[i].append((x, y))

# print (star)

# union(no cycle)
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

# find
def _find(i):
    if p[i] != i:
        p[i] = _find(p[i])
    return p[i]

#두 점 사이의 거리  √((X2 -X1)^2 + (y2-y1)^2)
def distance(tu1, tu2):
    dx = math.pow(tu1[0] - tu2[0], 2)
    dy = math.pow(tu1[1] - tu2[1], 2)
    dis = math.sqrt(dx + dy)
    return dis

# 경우의 수 악수하듯 나와 내 뒤에 있는 점들 사이의 거리를 구해서 간선의 비용으로 설정
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i != j:
            d = distance(star[i][0], star[j][0])
            heapq.heappush(edge, (d, i, j))
            
# print(edge)            
            
while edge:
    cost, a, b = heapq.heappop(edge)
    if _union(a, b): # 사이클이 생기지 않는 경우에만 거리(비용)을 더해준다.
        total += cost

print(total)