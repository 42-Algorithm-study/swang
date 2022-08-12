# 서로소 집합 알고리즘
# 1. union 연산을 확인하여 서로 연결된 두 노드 A, B 확인
# 2-1.  A와 B의 루트노드 A', B'을 각각 찾는다.
# 2-2. 루트 노드 중 더 작은수를 루트노드로 갱신한다.
#       if (A' < B') B의 루트노드는 A'
# 3. 모든 union 연산을 처리할 때까지 반복한다.

# 원소 == 노드, union == 간선

N, M = map(int, input().split()) # 원소 개수, union 연산 개수

parent = []
_set = []
for i in range(0, N + 1):
    parent.append(i)


for i in range(M):
    A, B = map(int, input().split())
    p = min(parent[A], parent[B])
    parent[A] = p
    parent[B] = p
# 부모노드가 더 작은 애를 뽑아서 부모노드를 넣어줌-> 집합을 합치는 과정이 맞나?


# 부모노드 정리
def set_parent(me, parent):
    if parent[me] != me:
        return set_parent(parent[me], parent)
    else:
        return me
# 이 부분은 find_parent로 함수이름을 선언했다면 더 좋았겠다.

_set.append(0)
for i in range(1, N + 1):
    _set.append(set_parent(i, parent))
# 부모 노드를 굳이 리스트에 저장하지않고, 출력시 바로 반환하도록 하도록 개선할 수 있음.
    

# 각 원소가 속한 집합
print("각 원소가 속한 집합 :", end=" ")
for i in range(1, N +1 ):
    print(_set[i], end=" ")
print()


# 각 원소의 부모 노드
print("각 원소의 부모 노드 :", end=" ")
for i in range(1, N +1 ):
    print(parent[i], end=" ")