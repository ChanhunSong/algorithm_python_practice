"""
큐를 사용하여 풀이

빈리스트 한번 돌리자
"""
import sys

sys.stdin = open("test.txt", "r")
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n, k = map(int, input().split())

    upque = deque([[0,i,0] for i in range(n)])
    downque = deque([[0,n+i,0] for i in range(n)])


    inlist = list(map(int, input().split()))

    for i, v in enumerate(inlist):
        if i < n:
            upque[i][0] =v
        else:
            downque[i%n][0]  =v

    count = 0
    upque.reverse()
    downque.reverse()
    print(n, k ,upque, downque)
    flag = 0
    

    while(count < k):
        #컨베이어 벨트 동
        flag +=1

        cur = deque.popleft(upque)
        cur[2] = 0
        downque.append(cur)
        nex = deque.popleft(downque)
        upque.append(nex)
        #print(cur, nex)

        for i in range(n):
            if i == 0:
                upque[0][2] = 0
            else:
                if upque[i-1][2] == 0 and upque[i-1][0] > 0  and upque[i][2] == 1 :
                    upque[i-1][0] -=1
                    if upque[i-1][0] == 0:
                        count += 1
                    upque[i-1][2] = upque[i][2]
                    upque[i][2] = 0

        if upque[-1][2] == 0 and upque[-1][0] > 0 :
            upque[-1][2] = 1
            upque[-1][0] -=1
            if upque[-1][0] == 0:
                count += 1


        
        

        #내구도 감소
    print(flag)


    

    
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n, k = map(int, input().split())

    upque = deque([[0,i,0] for i in range(n,0,-1)])
    downque = deque([[0,i,0] for i in range(2*n,n,-1)])


    inlist = list(map(int, input().split()))

    for i, v in enumerate(inlist):
        if i < n:
            upque[n-1-i][0] =v
        else:
            downque[(i-n)][0]  =v

    count = 0
    print(n, k ,upque, downque)
    flag = 0 

    while(count < k):
        #컨베이어 벨트 동

        cur = deque.popleft(upque)
        downque.append(cur)

        nex = deque.popleft(downque)
        upque.append(nex)
        #print(cur, nex)

        upque[0][2] = 0
        #로봇 이동 및 내구도 감소
        for i in range(1, len(upque)):

            if upque[i-1][2] == 0 and upque[i-1][0] > 0:
                upque[i-1][2] = upque[i][2]
                upque[i-1][0] -= 1
        if upque[-1][0] > 0:
            upque[-1][2] = 1
            upque[-1][0] -= 1

        if upque[-1][0] == 0:
            count += 1
        flag +=1

        #내구도 감소
    print(downque[-1][1],flag)


"""
    

    

    
    
