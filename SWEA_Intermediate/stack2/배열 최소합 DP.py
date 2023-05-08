
'''
재귀로 구현한 것을 while 과 스택으로

부분 행렬 생성을 set으로 대체 < 이것부터 구현

'''


import sys

sys.stdin = open("sample_input.txt", "r")

import heapq

global run
run = 0

def recusion(n, min_num_list, n_set , sumnum, input_matrix , x_set , y_set):
#가지치기
    global run
    run +=1
    if min_num_list[0] <= sumnum:
        return 0 #추후 수정
    # 종료조건
    if n == 1:
        x_res = n_set - x_set
        y_res = n_set - y_set
        sumnum += input_matrix[x_res.pop()][y_res.pop()]
        if min_num_list[0] > sumnum:
            min_num_list[0] = sumnum
        return 1 #추후 수정
    #print(n, min_num_list , sumnum , x_set , y_set)
    heap = list()
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix)):
            if i in x_set or j in y_set:
                continue
            x = x_set | set([i])
            y = y_set | set([j])
            heapq.heappush(heap , (input_matrix[i][j] , x, y))

    while heap:
        cur = heapq.heappop(heap)
        cur_num , x_set , y_set = cur
        recusion(n-1, min_num_list ,n_set , sumnum+ cur_num, input_matrix, x_set , y_set)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    input_matrix = [[] for _ in range(n)]
    for i in range(n):
        input_matrix[i] = list(map(int, input().split()))
    min_num_list= [10**10]
    n_set = set([i for i in range(n)])
    recusion(n, min_num_list ,n_set , 0, input_matrix,set(),set())

    
            

    print("#{} {} {}".format(test_case, min_num_list[0], run))
