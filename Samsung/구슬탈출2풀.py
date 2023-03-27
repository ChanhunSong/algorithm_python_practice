"""

기본전략
입력을 그대로 받는다.
기능도 요구사항 그대로 진행
공통된 기능은 함수로 선언한다.
재귀함수로 구현해야한다면 내부에 while을 선언하여 해결한다. >> 이생각을 못했...ㅎㅎ


입력을 받아서 bfs(거리를 리턴해야 하기 때문)
조심해하는 부분 > 구슬이 겹칠때를 고려해야한다.(이동 함수가 실행될때 마다)

"""
import sys

sys.stdin = open("rbtest.txt", "r")
from collections import deque


def move():
    pass
    


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(input())

    #print(graph)
    rx, ry, bx,by = 0, 0, 0, 0
    depth = 0
    vlist = [[[False]*m for _ in range(n)] , [[False]*m for _ in range(n)]]

    
    for i in range(n):
        for j in range(m):
            if graph[i][j]  == "R":
                graph[i][j] = "."
                rx = i
                ry = j
            if graph[i][j]  == "B":
                graph[i][j] = "."
                bx = i
                by =j
    que = deque([0, rx, ry, bx, by])
    res = -1


    whlie(que):
        depth, rx, ry, bx, by = deque.popleft(que)

        

    
    print(rx, ry, bx,by)
    
