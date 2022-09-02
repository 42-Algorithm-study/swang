# https://www.acmicpc.net/problem/2960

import math

N, K = map(int, input().split())

arr = [True for _ in range(N + 1)]

count = 0
for i in range(2, N + 1): # 지울 수 있는 모든 수를 지워야 하므로 범위를 N+1로 설정
    if arr[i]:
        j = 1
        while i * j <= N:
            if arr[i*j]: # 중복으로 지우는 케이스는 더하지 않기 위해서 True값을 가질때만 지움
                arr[i*j] = False
                count += 1
                if count == K:
                    print(i*j)
                    exit(0)
            j += 1
