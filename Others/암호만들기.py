# https://www.acmicpc.net/problem/1759

import itertools

# 알파벳에서 모음은 5개
m = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
data = list(input().split())

# abc는 되지만 bac는 안됨 (abc로 조합을 선점하면 bac는 알아서 걸러짐)
# -> 알파벳 순으로 `정렬`해서 `조합`하기
data.sort()
for case in itertools.combinations(data, L):
    count = 0
    for i in case: # 조합된 case에서 알파벳 하나씩 추출
        if i in m:  # 그 알파벳이 m에 있다면
            count += 1 # 개수 += 1
    if count >= 1 and L - count >= 2:
		# 모음이 1개이상이고, 전체 길이 - 모음개수 == 자음개수가 2개 이상일 때만
        print("".join(case)) # 출력