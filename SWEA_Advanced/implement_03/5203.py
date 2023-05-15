"""
1차 풀이 - 시간 0:13:54
강의에서 봄

리스트 만들어줌

check_run() 함수 만듬

triplet 함수 만듬

번갈아가면서 리스트 어펜드하고 함수 돌리기

think : 2:44
"""


import sys

sys.stdin = open("5203_sample_input.txt", "r")

T = int(input())


def check_run(p):
    for i in range(len(p)-2):
        if p[i] and p[i+1] and p[i+2]:
            p[i] -=1
            p[i+1] -=1
            p[i+2] -=1
            return True

    return False


def check_triplet(p):
    for i, num in enumerate(p):
        if num >= 3:
            p[i] -=3
            return True


    return False


for test_case in range(1, T + 1):
    res = 0
    in_card = list(map(int, input().split()))
    p1 = [0 for _ in range(10)]
    p2 = [0 for _ in range(10)]
    in_card.reverse()
    while(in_card):
        p1[in_card.pop()] += 1
        p2[in_card.pop()] += 1
        if check_run(p1) or check_triplet(p1):
            res = 1
        elif check_run(p2) or check_triplet(p2):
            res = 2

        if res:
            break



    print("#{} {}".format(test_case, res))