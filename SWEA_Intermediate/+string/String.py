"""
데자뷰...?

인덱스를 신경쓰지 않고 하겠다.
"""


import sys
sys.stdin = open("test_input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    t = input()
    target = input()
    t_len = len(target)
    string = input()
    res_dict = dict()
    res_dict[target] = 0

    for i in range(len(string)):
        if string[i:i+t_len] in res_dict:
            res_dict[target] += 1
    print("#{} {}".format(test_case ,res_dict[target]))
