from collections import deque
import copy

v = int(input())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

time = [0] * (v + 1)

for i in range(1, v + 1):
    lines = list(map(int, input().split()))
    time[i] = lines[0]
    for j in range(1, len(lines)):
        pre = lines[j]
        if pre == -1:
            break
        graph[pre].append(i)
        indegree[i] += 1

# ret = time
# ㄴ> ret 리스트를 변경하면 time에도 변경이 일어나서 시간이 중복으로 더해짐!
# 깊은 복사를 이용해야한다.
ret = copy.deepcopy(time)

def topology_sort(v):
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        subject = q.popleft()
        for next in graph[subject]:
            ret[next] = max(ret[next], ret[subject] + time[next])
            # 진입 차수가 0인 노드들부터 총 수강시간을 계산하므로,
            #         어떤 과목을 수강하기 까지의 총 수강시간 = 그 과목의 직전 선수과목의 총 시간 + 그 과목을 듣는 시간
            # 한 과목으로 오는 커리큘럼이 여러개일 경우 더 오래걸리는 시간을 기입한다.
            #
            # next 과목의 결과테이블에 담긴 시간 vs 결과테이블에 저장된 subject까지 수강하는 시간 + next 과목을 듣는 시간
            # next과목의 결과 테이블은 초기에 그 과목만을 수강하는 시간이 담겨있음
            #             한번 갱신이 이루어지면, 그 과목의 총 수강시간으로 담겨짐
            #                        그 과목까지의 커리큘럼이 여러갈래라면, 더 오래 걸리는 시간으로 갱신하기 위해 max()로 비교
            # subject의 결과 테이블은 그 과목까지의 총 시간이 담겨있음
            #       처음부터 진입차수가 0인 과목들은 따로 더할 수강 시간이 없으므로 본인 과목의 수강시간만 결과 테이블에 담기게 된다.
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

topology_sort(v)

print(ret)