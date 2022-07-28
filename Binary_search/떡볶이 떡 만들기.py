N, M = map(int, input().split())
rice = list(map(int, input().split()))

def cut(arr, custom, start, end):
    total = 0
    cut_point = (start + end) // 2
    for a in arr:
        if (a - cut_point > 0):
            total += a - cut_point
    if total == custom:
        return cut_point
    elif total > custom:
        return cut(arr, custom, cut_point, end)
    elif total < custom:
        return cut(arr, custom, start, cut_point)

print(cut(rice, M, 0, max(rice)))

# 떡볶이 떡을 자르는 방법
# 1. 제일 긴 떡의 길이를 기준으로 절반으로 자른다
# 2-1 잘린 떡의 길이의 합이 손님이 원하는 길이보다 작다면, 더 길게 잘리도록 cut_point를 감소
# 2-2 잘린 떡의 길이의 합이 손님이 원하느 길이보다 크다면, 더 작게 잘리도록 cut_point를 증가
# cut_point를 증가시키거나 감소시킬때의 비율은 이진 탐색에 맞게 포인트부터 끝단을 기준으로 절반씩 이동시킨다.
# cut(arr, custom, start + 1) 이런건 이분탐색이 아님. 처음만 반절 잘라서 들어가서 그 다음부터는 1씩 이동하며 찾고있음