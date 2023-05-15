"""

이거 그냥 강의실 문제


"""


import sys

sys.stdin = open("5202_sample_input.txt", "r")

T = int(input())



for test_case in range(1, T + 1):
    n = int(input())
    truck_list = [ list(map(int, input().split())) for _ in range(n)]
    #print(truck_list)
    res = 0

    truck_plan = sorted(truck_list, key = lambda x : x[1])
    #print(truck_plan)

    end_time = 0
    for truck in truck_plan:
        if truck[0] >= end_time:
            res +=1
            end_time = truck[1]



    print("#{} {}".format(test_case, res))