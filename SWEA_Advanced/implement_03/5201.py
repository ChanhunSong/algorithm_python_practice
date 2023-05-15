
"""
sol 0:10:55

0:03:00

트럭 한개당 하나만 적재 가능!

전체의 무게가 얼마인가?

가장 무거운 순으로 트럭, 화물 정렬

하나씩 비교하면서 넣을 수 있으면 트럭 줄이고 아님 통과

처음 트럭수와 연산후 트럭 수가 같으면 0....?

rse를 0으로 초기화 시키고 싫는 무게를 더해주기!

"""

import sys

sys.stdin = open("5201_sample_input.txt", "r")

T = int(input())



for test_case in range(1, T + 1):
    res = 0
    c_num, truck_num = map(int, input().split())
    contain_list = list(map(int, input().split()))
    truck_list = list(map(int, input().split()))

    # 정렬
    contain_list.sort(reverse = True)
    truck_list.sort()

    for con in  contain_list:
        if truck_list and truck_list[-1] >= con:
            truck_list.pop()
            res += con



    print("#{} {}".format(test_case, res))