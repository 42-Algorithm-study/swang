import heapq

# 최소 힙
def min_heap(iterable):
    h = []
    ret = []
    # 들어온 인자들을 모두 힙을 이용해 삽입한다.
    for data in iterable:
        heapq.heappush(h, data) # 힙을 이용해 h에 data를 추가
    for i in range(len(h)):
        ret.append(heapq.heappop(h)) # 힙을 이용해 h에서 데이터를 추출하여 ret에 삽입
    return ret
    
result = min_heap([1,3,5,7,9,2,4,6,8,0])
print(result)


# 최대 힙
def max_heap(iterable):
    h = []
    ret = []
    for data in iterable:
        heapq.heappush(h,-data) # 힙에 데이터를 추가할 때 음수로 변환
    for i in range(len(h)):
        ret.append(-(heapq.heappop(h))) # 데이터를 꺼낼 때 다시 양수로 전환
    return ret

result = max_heap([2,4,6,8,0,1,3,5,7,9])
print(result)        