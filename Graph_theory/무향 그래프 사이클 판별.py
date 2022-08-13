# 모든 간선에 대해 union 연산 전 서로의 부모 노드가 같은지 체크
# 부모 노드가 다르다면 union 연산, 부모 노드가 같다면 사이클 발생!
# 간선에 방향성이 없는 무향 그래프에서만 적용 가능.

def _union(A, B):
    a = p[A]
    b = p[B]
    if a < b:
        p[B] = a
    else:
        p[A] = b

def _find(i):
    if i != p[i]:
        p[i] = _find(p[i])
    return i

V, E = map(int, input().split())
p = [0] * (V + 1)
cycle = False

for i in range(0, V + 1):
    p[i] = i

for i in range(E):
    A, B = map(int, input().split())
    if (p[A] == p[B]):
        cycle = True
        break;
    _union(A,B)


if cycle:
    print("True")
else:
    print("False")