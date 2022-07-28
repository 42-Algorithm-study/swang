N = int(input())
bolt = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

bolt.sort()
find.sort()

def binary_search(arr, target, start, end):
    if start == end and arr[start] != target:
        return False
    mid = (start + end) // 2
    if (arr[mid] == target):
        return True
    elif arr[mid] > target:
        return(binary_search(arr, target, 0, mid - 1))
    elif arr[mid] < target:
        return(binary_search(arr, target, mid + 1, end))

for i in find:
    if (binary_search(bolt, i, 0, N) == True):
        print("yes", end=" ")
    else:
        print("no", end=" ")