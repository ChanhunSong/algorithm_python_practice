"""
10분


"""

import sys

sys.stdin = open("5204_sample_input.txt", "r")


def merge_sort(target):
    #종료
    if len(target) <= 1:
        return 0, target

    #분할
    else:
        num1, left = merge_sort(target[:len(target)//2])
        left.reverse()
        num2, right = merge_sort(target[len(target)//2:])
        right.reverse()

    #병합
    res = list()
    cur = num1 + num2
    if left[0] > right[0]:
        cur += 1
    while(left and right):
        # 왼쪽이 작은 경우
        if left[-1] <= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    while(left or right):
        if left:
            res.append(left.pop())
        if right:
            res.append(right.pop())

    return cur, res


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    target = list(map(int, input().split()))

    num_res, fin_res = merge_sort(target)

    print("#{} {} {}".format(test_case, fin_res[n//2], num_res))
