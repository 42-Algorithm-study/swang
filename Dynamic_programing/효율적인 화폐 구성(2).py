# 효율적인 화폐 구성 개선판

INF = int(10e9)

N, M = map(int, input().split())
money = list()

for i in range(N):
    money.append(int(input()))

# 계산한 값과 비교해서 최솟값으로 갱신하기 위해서 일부러 큰 수를 넣음, -1로 초기화 했을 떈 -1일 경우를 따로 고려해야했음...
dp = [INF] * (M + 1)

# 화폐 단위와 똑같은 애들은 1로 초기화
for m in money:
    if (m <= M): # 화폐단위보다 만들어야 하는 금액이 작을 수도 있다
        dp[m] = 1

# 최소 단위 화폐 + 1 부터  인덱스시작 (최소단위 화폐는 어차피 1로 초기화 되어있음)    
min_money = min(money)
for i in range(min_money + 1, M + 1):
    for m in money: # 각 화폐단위를 돌면서 계산
        if (i - m > 0): # 인덱스 범위 주의
            dp[i] = min(dp[i], dp[m] + dp[i - m]) # dp[i]가 INF든 계산한 개수가 들어있든 어쨌든 작은거 반환해서 갱신
# print(dp)
if (dp[M] == INF):
    print(-1)
else:
    print(dp[M])