# boj 1929
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오

import math

m, n = map(int, input().split())

arr = [True for _ in range(n + 1)]
arr[1] = False # 입력값 M, N이 1부터 들어옴!

for i in range(2, int(math.sqrt(n)) + 1): # 소수판별이므로 2부터 돌면서 소수체크를 해야함 m부터 아님
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(m, n + 1):
    if arr[i]:
        print(i)
