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
    reverse_input_matrix = [[] for _ in range(n)]
    trans_matrix = list()
    reverse_trans_matrix = list()

    for i in range(n):
        input_matrix[i] = tuple(map(int, input().split()))
        reverse_input_matrix[i] = input_matrix[i][::-1]

    for row in zip(*input_matrix):
        trans_matrix.append(row)
        reverse_trans_matrix.append(row[::-1])
        
    input_matrix = tuple(input_matrix)

    
    n_set = set([i for i in range(n)])
    greedy_nums = (greedy(n_set, input_matrix) ,greedy(n_set, reverse_input_matrix),greedy(n_set, trans_matrix),greedy(n_set, reverse_trans_matrix)     )
    print(greedy_nums)
    min_num = min(greedy_nums)
    stack = [(0,set())]

    if min_num*4 == sum(greedy_nums):
        stack = []

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
    
