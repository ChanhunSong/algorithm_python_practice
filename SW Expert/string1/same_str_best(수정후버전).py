
import sys

import time

sys.stdin = open("text_input.txt", "r")

start = time.time()
T = int(input())

for test_case in range(1, T + 1):
    n , m  = map(int, input().split())
    t_list = [input() for _ in range(n)]
    temp = list()
    pre_list = list()
    #zip이랑 enumerate 같이 쓰면 안됨?
    for item in t_list:
        temp.append(tuple(item))
    for item in zip(*temp):
        pre_list.append("".join(item))
