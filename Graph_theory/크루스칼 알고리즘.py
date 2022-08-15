# 크루스칼 알고리즘
import heapq

n, m = map(int, input().split())
p = [0] * (n + 1)
edge = []
span = []
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

for i in range(1, n + 1):
  p[i] = i

for i in range(m):
  a, b, cost = map(int, input().split())
  heapq.heappush(edge, (cost, a, b))

while edge:
  cost, a, b = heapq.heappop(edge)
  if _union(a, b):
    span.append((a,b))
    total += cost

print(span) ## 선택한 간선
print(total) ## 최소 비용