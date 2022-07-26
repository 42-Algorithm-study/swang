# 미래도시
# 플로이드 와샬 알고리즘

# N은 도시의 수, M은 도로의 수
N, M = map(int, input().split())

# 거리정보가 담길 그래프를 무한으로 초기화 (graph[N][N]의 접근을 위해 (N+1)^2 크기로 설정)
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 길의 시간은 0으로 초기화
for i in range(N + 1):
    graph[i][i] = 0

# 도로 연결 정보를 그래프에 추가(모든 도시간 이동 시간은 1)
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 방문 판매 목적지 dst, 소개팅 meet 입력받기
dst, meet = map(int, input().split())

# 모든 정점부터 visit을 거쳐가는 다른 모든 정점까지의 최단 시간 조사
# 거쳐갈 도시 1부터 N까지 * 출발도시 1부터 N까지 * 도착도시 1부터 N까지 N^3의 시간복잡도를 가짐
for visit in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # visit을 거쳐서 가는게 더 빠르면, visit을 들렸다가는 총 시간을 기입
            if (graph[i][j] > graph[i][visit] + graph[visit][j]):
                graph[i][j] = graph[i][visit] + graph[visit][j]

# 총 시간 cost 는 출발도시 1에서 소개팅도시 meet을 가는 시간 + 소개팅 도시 meet에서 방문판매도시 dst까지 가는 시간
cost = graph[1][meet] + graph[meet][dst]

# cost가 INF 보다 같거나 크다는 것은 도시가 연결되어있지 않다는 것
if cost >= INF:
    print(-1)
else:
    print(cost)