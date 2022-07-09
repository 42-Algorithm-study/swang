# 파이썬에서 정렬 문제
```python
# 위에서 아래로
n = int(input())

s = list()
for i in range(n):
    s.append(int(input()))
s.sort(reverse=True)
print(*s, sep="\n")
```

- `sort(reverse=True)` : 기본 sort()는 오름차순으로, 역순(내림차순)으로 정렬하도록 옵션을 추가할 수 있음
- `print(*s)` : 리스트의 요소를 출력
- `print(*s, sep="\n")` : 출력 요소들을 개행으로 구분하여 출력  
</br>  
</br>  
```python
# 성적낮은 순서
n = int(input())

student = list()
for i in range(n):
    student.append(input().split())
    student[i][1] = int(student[i][1])
student.sort(key=lambda x:x[1])

for i in range(n):
    print(student[i][0], end=" ")
```

- `input().split()` 자체가 이미 리스트임
- 두번째 요소만 int형으로 바꿔줌
- `sort(key=lambda x:x[1])` : 학생 리스트의 두번째 요소로 정렬하겠다는 람다 표현식
- 스페이스바로 구분하여 첫번째 요소만 출력  

