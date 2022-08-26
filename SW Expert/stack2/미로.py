"""
dfs, bfs 둘다 가능하지만 pruning을 적용하는 것은 최단거리를 고려하는 다익스트라
알고리즘이다.

따라서 다익스트라 알고리즘으로 풀어보겠다.

패딩은 인덱스 계산에서 자유롭게 하지만 뎁스가 1씩 늘어나는것과 같기에 효율성을 위해 사용하지 않겠다.

"""

import sys

sys.stdin = open("sample_input.txt", "r")
import heapq
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n =  int(input())
    graph = [[] for _ in range(n)]
    v_list = [[True]*n for _ in range(n)]
    """
    for i in range(n):
        graph[i] = list(map(int, list(input())))
        # 아 어차피 스타트랑 엔드를 찾아야 하네
        """
    start , end = 0 ,0
    for i in range(n):
        input_str = input()
        for j in range(n):
            if input_str[j] == "2":
                start = (i,j)
            if input_str[j] == "3":
                end = (i,j)
            graph[i].append(int(input_str[j]))
    #print(graph, start, end)

    heap = [(0,start)]
    v_list[start[0]][start[1]] = False
    vectors = ( (1,0), (-1,0) , (0,1), (0,-1))
    res = 0
    while(heap):
        cur = heapq.heappop(heap)
        #print(cur)

        for vec in vectors:
            ne = (vec[0] + cur[1][0] , vec[1] + cur[1][1])
            if ne[0] >= 0 and ne[0]<n and ne[1] >= 0 and ne[1]<n and v_list[ne[0]][ne[1]]:
                value = graph[ne[0]][ne[1]]

                if value== 3:
                    res =1
                    break
                elif value == 0:
                    v_list[ne[0]][ne[1]] = False
                    heapq.heappush(heap , (cur[0]+1 , ne))
    print("#{} {}".format(test_case , res))
