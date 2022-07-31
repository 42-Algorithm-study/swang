# 1로만들기
X = int(input())

a = [0] * (X + 1)
# a[X]에 값을 넣으려면 사이즈를 하나 크게 설정하는걸 잊지 말자!

a[2] = 1
a[3] = 1

i = 4
while (i <= X):
    if (i % 2 == 0):
        a[i] = a[i // 2] + 1
    if(i % 3 == 0):
        if a[i] == 0:
            a[i] = a[i // 3] + 1
        else:
            a[i] = min(a[i], a[i // 3] + 1)    
    if(i % 5 == 0):
        if a[i] == 0:
            a[i] = a[i // 5] + 1
        else:
            a[i] = min(a[i], a[i // 5] + 1)
    else:
        if a[i] == 0:
            a[i] = a[i - 1] + 1
        else:
            a[i] = min(a[i], a[i - 1] + 1)
    i += 1
# 반복문을 거치면서 a[i]이 0 일땐 새로 추가, 0이아니라면 최솟값으로 값을 넣어준다.

print(a[X])