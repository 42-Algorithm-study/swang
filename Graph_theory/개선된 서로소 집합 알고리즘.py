# 경로 압축 기법을 이용하여 부모노드를 설정
# 자신의 부모노드를 찾는 부분을 재귀로 구현


def _union(A, B):
  a = _find(A)
  b = _find(B)
  # **루트노드의 부모**를 바꿔줘야함!!
  # 루트노드의만 바꿔주면 하위 노드들은 알아서 따라옴
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def _find(i):
  if i != parent[i]:
    parent[i] = _find(parent[i])
  return parent[i]

V, M = map(int, input().split())
parent = []

for i in range(V + 1):
  parent.append(i)

for i in range(M):
  A, B = map(int, input().split())
  _union(A, B)


print("서로소 집합")
for i in range(1, V+1):
  print(_find(i), end=" ")
print()

# find 연산을 통해 parent 테이블이 새로 갱신되어있음
print("부모 테이블")
for i in range(1, V + 1):
  print(parent[i], end=" ")
print()