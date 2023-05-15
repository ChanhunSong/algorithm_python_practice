"""

리스트 받음

이진 탐색에서 번갈아 실행되면 1리턴되게 구현

binary_search(l, r, inlist)


    return l and r , inlist

전략 : 7:00

GG : 45분

"""




import sys

sys.stdin = open("5207_sample_input.txt", "r")

def binary_search(l, r, inlist, tar, lf, rf):
    print(l, r, inlist, tar, lf, rf)
    cur_num = 0
    m = (l + r) // 2
    if inlist[m] == tar:
        if lf and rf:
            cur_num = 1
        return cur_num, m
    # 못찾음 중 벗어나는 것만
    elif l > r:
        return 0, -1
    # 좌탐
    elif inlist[m] > tar:
        cur_num, index = binary_search(l, m-1, inlist, tar, lf + 1, rf)
    # 우탐
    elif inlist[m] < tar:
        cur_num, index = binary_search(m+1, r, inlist, tar, lf , rf + 1)
    return cur_num, index

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_num, target_num = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()
    target_list = list(map(int, input().split()))
    res = 0
    for tar in target_list:
        if input_list[(len(input_list)-1)//2] == tar:
            res += 1
        else:
            cur_res, index = binary_search(0, len(input_list)-1, input_list, tar ,0,0)
            res += cur_res

    print(f"#{test_case} {res}")