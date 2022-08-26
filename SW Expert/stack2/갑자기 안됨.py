import sys
sys.stdin = open("sample_input.txt", "r")
import heapq



T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    input_matrix = [[] for _ in range(n)]
    for i in range(n):
        input_matrix[i] = tuple(map(int, input().split()))
    input_matrix = tuple(input_matrix)
    min_num= 10**10
    n_set = set([i for i in range(n)])
    run_heap = [(0, n ,set(),set())]
    while(run_heap):
        #print(run_heap[0])
        sumnum , n  , x_set , y_set = run_heap.pop()
        if min_num <= sumnum:
            continue

        x_res = n_set - x_set
        y_res = n_set - y_set
        if n == 1:
            sumnum += input_matrix[x_res.pop()][y_res.pop()]
            if min_num > sumnum:
                min_num = sumnum
        for i in x_res:
            for j in y_res:
                x = x_set | set([i])
                y = y_set | set([j])
        
                #print(sumnum)
                temp = input_matrix[i][j]+sumnum
                if temp > min_num:
                    continue
                #print(input_matrix[i][j]+sumnum , temp)
                run_heap.append((temp, n-1 , x, y))

    print("#{} {}".format(test_case, min_num))
