"""
n =10 일때

중복조합으로 본다면

100 C 10 = 17,310,309,456,440

각열 인덱스의 순열로 본다면

3628800

그리디로 값을 하나 뽑고 가지치기 시작

순열로 구현하면 되는구나..!
"""

import sys
sys.stdin = open("sample_input.txt", "r")


def greedy(n_set, input_matrix):
    t_set = set()
    res = 0
    for row in input_matrix:
        cur_set = n_set - t_set
        min_num = 10**10
        min_i = 0

        for i in cur_set:
            if min_num > row[i]:
                min_num = row[i]
                min_i = i
        res += min_num
        t_set.add(min_i)
    return res
    


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    input_matrix = [[] for _ in range(n)]
    for i in range(n):
        input_matrix[i] = tuple(map(int, input().split()))
    input_matrix = tuple(input_matrix)
    n_set = set([i for i in range(n)])
    min_num = greedy(n_set, input_matrix)

    stack = [(0,set())]

    while(stack):
        #print(stack[-1])
        sumnum, c_set = stack.pop()
        res_set = n_set - c_set
        if len(c_set) == n and min_num > sumnum:
            min_num = sumnum

        for i in res_set:
            num = input_matrix[len(c_set)][i]
            up_set = c_set | set([i])
            temp = sumnum + num
            if sumnum > min_num:
                continue
            stack.append((sumnum + num , up_set))

    print("#{} {}".format(test_case, min_num))
    
