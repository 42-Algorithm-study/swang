# 1774 우주신과의 교감
import heapq
import math
import sys

input = sys.stdin.readline

# 점과 점 사이의 거리
def dis(tu1, tu2):
    dx = tu1[0] - tu2[0]
    dy = tu1[1] - tu2[1]
    d = math.sqrt(pow(dx,2) + pow(dy,2))
    return d

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

N, M = map(int, input().split())

p = [i for i in range(N + 1)]

position = [(0,0)]    
edge = []
total = 0

# 좌표 수집
for i in range(1, N + 1):
    x, y = map(int, input().split())
    position.append((x, y))

#이미 연결된 통로에 대한 유니온 연산
for i in range(M):
    a, b = map(int, input().split())
    # 이미 연결된 통로가 사이클이 없다는 보장은 없다.
    _union(a, b)

# 좌표들 간 거리정보 저장
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        d = dis(position[i], position[j])
        heapq.heappush(edge, (d, i, j))

while edge:
    cost, a, b = heapq.heappop(edge)
    # 최소 비용 간선을 꺼내면서, 사이클이 발생하지 않을 때만 비용을 더해줌
    # (위에서 이미 건설된 통로는 이미 합집합 연산 완료)
    if _union(a, b):
        total += cost

# 소수점 둘째자리까지 출력
print('%.2f' %total)


# 구해야 하는 것 : 이미 연결된 노드를 활용하여 추가건설한 추가비용
# 풀이 방법 : 이미 연결되어 있던 통로들은 합집합 연산을 해준다.

# 이미 연결된 노드들은 부분 집합의 느낌
# -> 모든 노드를 연결해야 하므로 어떻게든 그 부분집합과 연결을 해야함
# -> 최소 비용 간선부터 합집합 연산을 하므로, 부분집합 덩어리와 가장 가까운 통로가 건설 될 것.
# 사이클이 생기지 않을 때만 건설하므로, 이미 연결된 간선을 또 연결하려고하면 비용이 더해지지 않음

# 부분 집합들과 유니온 연산을 하되, 사이클이 발생하지 않도록하면
# 추가 건설 비용을 구할 수 있음

# 이미 연결된 노드들 간의 비용을 0으로 하여 푸는 방법도 있음
# (최소 힙에서 꺼낼 때 비용이 0인 간선들부터 꺼내질 것)