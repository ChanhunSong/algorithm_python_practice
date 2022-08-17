
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    t_string = input()
    s_string = input()
    res = 0
    if t_string in s_string:
        res = 1
    print("#{}".format(test_case) , res)
