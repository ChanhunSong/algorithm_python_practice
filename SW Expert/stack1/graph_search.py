
"""
- 행렬?
- 리스트?

리스트!

dfs , bfs 둘다 가능


"""

import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, e = map(int , input().split())
    graph = [[] for _ in range(n+1)]
    res = 0
    for _ in range(e):
        n1, n2 = map(int , input().split())
        graph[n1].append(n2)
    start , end  = map(int , input().split())
    #stack
    stack = list()
    #visit
    v_list = [True]*(n+1)
    v_list[start] = False
    for n in graph[start]:
        stack.append((start, n))
    while(stack):
        cur = stack.pop()
        if cur[1] == end:
            res = 1
            break
        # 방문 ㄴㄴ
        if v_list[cur[1]]:
            v_list[cur[1]] = False
            for node in graph[cur[1]]:
                stack.append((cur[1] , node))
    print("#{} {}".format(test_case , res))

