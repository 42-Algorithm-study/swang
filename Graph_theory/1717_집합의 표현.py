## union-find

import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 설정
input = sys.stdin.readline

n, m = map(int, input().split())

p = [0] * (n + 1)
for i in range(n + 1):
    p[i] = i

def _find(i):
    if i != p[i]:
        p[i] = _find(p[i])
    return p[i]
    
def _union(a,b):
    # a,b 의 최상위 부모노드끼리 비교하고 그 최상위부모의 부모노드를 갱신하는식 
    # (하위 노드들은 나중에 최상위노드의 부모값을 갖게 될 것 : _find() 연산)
    a = _find(a) 
    b = _find(b)
    if a == b:
        return
    elif a < b:
        p[b] = a
    else:
        p[a] = b

for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        _union(a,b)
    elif c == 1:
        if _find(a) == _find(b):
            print('YES')
        else:
            print('NO')