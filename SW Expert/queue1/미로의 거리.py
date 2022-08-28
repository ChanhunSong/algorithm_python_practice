"""
??? 똑같은 문제를 푼 기억이 있는데

그거는 도달만 할 수 있으면 되서 dfs로도 풀었던거 같다.
"""

import sys

sys.stdin = open("sample_input.txt", "r")

import heapq
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    graph = [[] for _ in range(n)]
    start = 0
    end = 0

    res= 0 
    for i in range(n):
        graph[i] = list(input())
        for j , s in enumerate(graph[i]):
            graph[i][j] = int(graph[i][j])
            if graph[i][j] == 2:
                start = (i,j)
            if graph[i][j] == 3:
                end = (i,j)
    v_list = [ [True]*n for _ in range(n)]
    #print(graph,v_list,start)
    v_list[start[0]][start[1]] = False
    

    que = [(0,start)]
    vectors = ( (1,0) ,(-1,0) ,(0,1),(0,-1))
    flag = True
    while(que and flag):
        w , cur = heapq.heappop(que)

        for v in vectors:
            x , y = cur[0] + v[0] , cur[1] + v[1]
            if x >=0 and x < n and y >= 0 and y < n and v_list[x][y]:
                if graph[x][y] == 0:
                    heapq.heappush(que, (w+1 , (x,y)))
                    v_list[x][y] = False
                if graph[x][y] == 3:
                    res = w
                    flag = False
                    break
    print("#{} {}".format(test_case,  res))
