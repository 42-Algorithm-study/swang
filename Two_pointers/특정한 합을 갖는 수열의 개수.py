# 투포인터

n = int(input())
m = int(input())
count = 0
lst = []
for _ in range(n):
    lst.append(int(input()))


def too_pointer(start, end, lst):
    ret = 0
    for i in range(start, end + 1):
        ret += lst[i]
    return ret

start = 0
end = 0
while start < n:
    while end < n:
        _sum = too_pointer(start, end, lst)
        if (_sum == m):
            count += 1
            start += 1
            break
        elif(_sum < m):
            end += 1
        else:
            start += 1
            break
print(count)