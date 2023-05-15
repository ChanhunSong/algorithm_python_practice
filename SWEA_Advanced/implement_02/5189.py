"""
최소 경로 -> 다익스트라인데... 다시 돌아오는 조건에서도 쓸 수 있나?

그래프 탐색을 구현하면 가능하기는 함


인접 행렬로 양방향 그래프 주어짐

음... 이거 그냥 순열로 풀수 있나..? 그렇다...!

"""


import sys
import itertools
import heapq

sys.stdin = open("5189_sample_input.txt", "r")


T = int(input())

def per_sum(row, map_tuple):
    res = map_tuple[0][row[0]]

    for i, n in enumerate(row):
        #print(res)
        if i+1 < len(row):
            res += map_tuple[n][row[i+1]]
        else:
            res += map_tuple[n][0]

    return res

for test_case in range(1, T + 1):
    n = int(input())
    map_list = list()
    res = 10**10
    for i in range(n):
        map_list.append( tuple(map(int, input().split()))  )
    map_tuple = tuple(map_list)

    i_list = [i for i in range(1,n)]
    #print(i_list)
    for row in itertools.permutations(i_list, len(i_list)):
        res = min(res, per_sum(row, map_tuple))
        
    

    print("#{} {}".format(test_case , res))
