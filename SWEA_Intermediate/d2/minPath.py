import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def minPath(x,y,graph, maxnum):
    if x == len(graph)- 2 and y == len(graph)- 2:
        return graph[x][y]
    elif graph[x][y] == -1:
        return 10**10
    res1 = 10**10
    res2 = 10**10
    if x+1 <= len(graph)- 2:
        res1 = minPath(x+1,y,graph,maxnum)

    if y+1 <= len(graph)- 2:
        res2 = minPath(x,y+1,graph, maxnum)
    return graph[x][y] + min(res1 , res2)


for test_case in range(1, T + 1):
    n = int(input())
    
    graph = [ [-1]*(n+1) for _ in range(n+1) ]
    maxnum = 0
    for i in range(n):
        t_list = list(map(int, input().split()))
        for j , item in enumerate(t_list):
            graph[i][j] = item
            if item > maxnum:
                maxnum = item

    res = minPath(0,0,graph, maxnum)
    if res == 10**10 * n:
        res = maxnum * n
    print("#{} {}".format(test_case , res))
    
# 실행 안하고 인덱스로만 제어하는 것이 경우의 수를 줄여준다.
#> 특히 팩토리알로 늘어나는 문제였기에 더 중요했다.
