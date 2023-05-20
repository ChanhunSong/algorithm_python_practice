"""

충전

도착? 또는 갈 수 있는 범위 확인

범위 내에서 교채 배터리 + (현재 배터리 거리 - 배터리 위치)로 최대값 찾기

배터리 선택

"""


import sys

sys.stdin = open("5208_sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    res = 0
    oil_list = list(map(int, input().split()))
    oil_list = oil_list[1:] + [0]
    #print(oil_list)

    index = 0
    dis = 0
    next_i = 0
    while (index < len(oil_list)):
        dis = oil_list[index]
        print("end", index + dis , len(oil_list) - 1)
        if index + dis>= len(oil_list) - 1:
            break
        else:

            cur_oil_list = [x for x in zip(oil_list[index+1:index+1 + dis], [i for i in range(dis,-1,-1)])]
            #print(cur_oil_list)
            cur_oil_list.sort(key = lambda x : x[0] + (index + dis - x[1]))
            b, next_i = cur_oil_list[-1]
            index += (dis - next_i)
            res += 1




    print(f"{test_case} {res}")