# 선행문제가 있다면 반드시 선행문제를 푼다
# 가능하면 쉬운 문제 (문제번호가 작은순으로)
# -> 선행관계가 없는 문제들 중 "가능하면 쉬운 문제순"으로 풀어야 하므로
# 문제 번호가 작은 순으로 먼저 푼다.
import heapq

N, M = map(int, input().split())

indegree = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

def topology_sort():
    q = []
    ret = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i) # 문제들을 최소힙을 사용하여 관리
    while q:
        subject = heapq.heappop(q) # 최소힙이므로 진입차수가 0인 문제들 중 작은 수부터 pop
        ret.append(subject)
        for _next in graph[subject]:
            indegree[_next] -= 1
            if indegree[_next] == 0:
                heapq.heappush(q, _next) # 문제들을 최소힙을 사용하여 관리
    print(*ret)
    
topology_sort()