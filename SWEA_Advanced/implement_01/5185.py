
"""
문제 풀이 13분

전략

16진수를 정수로

정수를 2진수로

2진수의 0을 보완해주기

"""

import sys

sys.stdin = open("5185_sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    
    n , hex_s = list(input().split())
    n = int(n)
    cur_num = int("0x"+ hex_s, 16)
    cur_num = bin(cur_num)
    cur_num = cur_num[2:]
    while(len(cur_num) < n*4):
        cur_num = "0"+ cur_num
    
    print('#' + str(test_case) + " " + cur_num)
