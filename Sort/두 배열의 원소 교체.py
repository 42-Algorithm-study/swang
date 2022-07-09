from collections import deque

N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

A = deque()
B = deque()

for i in range(N):
    A.append(a[i])
    B.append(b[i])

for i in range (K):
    A.append(B.popleft())
    B.append(A.popleft())

# print(A)
print(sum(A))