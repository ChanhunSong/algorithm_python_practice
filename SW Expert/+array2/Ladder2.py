'''

정말 낯설게 느껴질만큼 기본적인 구현 문제

>> 아 C++ 이였으면 어려웠겠다.

여러 의심이 들지만

x의 좌표를 찾는다.

좌 우 위 순서로 벡터를 만든다.

y !=0 일때 1이면 전진

y== 0이면 x값 리턴

#설마 가지가 겹치는 놀라운 일은 구현하지 않았을것으로 기대함

num 더해서 최소값 리턴

'''


import sys
sys.stdin = open("input.txt", "r")

T = 10
vectors = ((0,1) , (0,-1) , (-1,0))
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    matrix = [[] for _ in range(100)]
    point_list = list()
    res_list = list()

    for i in range(100):
        matrix[i] = list(map(int , input().split()))

    for i in range(100):
        if matrix[99][i] == 1:
            point_list.append((99 , i))
    for point in point_list:
        end_point = point
        cnum = 0
        visit_matrix = [[1]*100 for _ in range(100)]
        while(end_point[0] > 0):
            #print(end_point)
            for v in vectors:
                y = end_point[0] + v[0]
                x = end_point[1] + v[1]
                #print(y,x ,matrix[y][x])
                if y >=0 and (x >= 0) and (x < 100) and matrix[y][x] ==1 and visit_matrix[y][x] ==1:
                    #print("run")
                    visit_matrix[end_point[0]][end_point[1]] =0
                    end_point = (y,x)
                    cnum += 1
                    break
        res_list.append((cnum , end_point))
    res_list.sort()
    print("#{} {}".format(t , res_list[0][1][1]))
