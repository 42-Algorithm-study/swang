# 접두사 합을 이용한 구간합 빠르게 계산하기

T = int(input())
lst = list(map(int, input().split()))

p = [0]

p_sum = 0

for l in lst:
    p_sum += l
    p.append(p_sum)
    

while T > 0:
    L, R = map(int, input().split())
    print(p[R]- p[L - 1])
    T -= 1