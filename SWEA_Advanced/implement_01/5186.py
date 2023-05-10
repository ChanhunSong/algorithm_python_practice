
"""
문제 풀이 0:15:00

가장 간단하게 푼다는 원칙을 지키지 않았다.

실수 이진수 변환 구현
    #13자리부터 오버플로 확인

"""

import sys

sys.stdin = open("5186_sample_input.txt", "r")


def convert(f):
    res = ""

    for i in range(1,13):
        f = f*2
        if f>=1:
            f -= 1
            res = res + "1"
        else :
            res = res + "0"
        if not f:
            break
    if f:
        res = "overflow"
    return res

T = int(input())

for test_case in range(1, T + 1):
    n = float(input())
    print('#' + str(test_case) + " " + convert(n))
    
