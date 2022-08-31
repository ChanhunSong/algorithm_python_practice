import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())
import heapq
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, e = map(int , input().split())
    graph = [[] for _ in range(n+1)]
    res = 0
    for _ in range(e):
        n1, n2 = map(int , input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    start , end  = map(int , input().split())
    que = [(0,start)]
    v_list = [True]*(n+1)
    while(que):
        w , cur = heapq.heappop(que)
        if cur == end:
            res = w
            break
        if v_list[cur]:
            v_list[cur] = False
            for node in graph[cur]:
                heapq.heappush(que,(w+1 , node))
    print("#{} {}".format(test_case , res))
