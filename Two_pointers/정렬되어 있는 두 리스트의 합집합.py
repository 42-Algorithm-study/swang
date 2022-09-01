#투포인터
#정렬 되어있는 두 리스트의 합집합

A = list(map(int, input().split()))
B = list(map(int, input().split()))

new = []
a = 0
b = 0

while a < len(A) and b < len(B):
    if A[a] <= B[b]:
        new.append(A[a])
        a += 1
    else:
        new.append(B[b])
        b += 1

if a == len(A):
    while b < len(B):
        new.append(B[b])
        b += 1
elif b == len(B):
    while a < len(A):
        new.append(A[a])
        a += 1

print(*new)