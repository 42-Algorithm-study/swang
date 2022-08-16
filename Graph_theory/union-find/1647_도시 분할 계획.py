import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

p = [0] * (n + 1)
for i in range(n + 1):
    p[i] = i
    
edge = []
total = 0

def _find(i):
  if p[i] != i:
      p[i] = _find(p[i])
  return p[i]

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

for i in range(m):
  a, b, cost = map(int, input().split())
  heapq.heappush(edge, (cost, a, b))

while edge:
  cost, a, b = heapq.heappop(edge)
  if _union(a, b):
    total += cost
    last = cost

print(total - last)
# 제일 비용이 큰 마지막 간선만 끊어버리면
# 하나의 마을엔 도로가 없는 집 한 채만 남게되므로
# 두 마을의 도로비용 합이 최소가 된다.

# 마을을 두개로 쪼개는데 하나의 마을에 집 한 채만 남는다는게..... 이상하긴 함. 