# 1로 만들기 개선판
# 어차피 min으로 비교할 거니까, 제일 간단한 식의 결과를 넣어두고 min으로 비교하자

X = int(input())

dp = [0] * (X + 1)

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1 #일단 1 빼는걸로 값을 넣어둠
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) # 2로 나누는 과정때문에 +1 더해주기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1) # 3로 나누는 과정때문에 +1 더해주기
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1) # 5로 나누는 과정때문에 +1 더해주기

print(dp[X])        