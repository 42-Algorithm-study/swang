# 투포인터

lst = list(map(int, input().split()))
m = int(input())
_len = len(lst)

count = 0
_sum = 0
end = 0

for start in range(_len):
    print(start, ",", end)
    while end < _len and _sum < m: # 조건은 end가 리스트의 길이를 넘지 않고, 리스트의 부분합이 m보다 작을 때
        _sum += lst[end]
        end += 1
    if _sum == m:
        count += 1
    _sum -= lst[start] # m보다 크다면 start를 옮기고, start 값만큼 빼줌 
    # 반복문을 탈출한 조건이 end가 _len을 벗어난거라면 다시 _end를 돌려놔야 하는거 아닌가?
    # end가 _len 을 벗어나서 탈출했다면, 리스트의 합이 m보다 작을 수 밖에 없음. start를 옮기면 합은 줄어들 수 밖에..

print(count)