

import sys

"""
1) 09:50
n*n

경사로 구현 문제 (구현) -> 이 부분이 잘 되면

-> 열 별로 구현 할것인가? ㅇㅇ

-> 좌표별로 할 것인가? ㄴㄴ




2) 10:45

자료구조 리스트

3) 14:3
-> 해당열이 활주로 건설 가능한지 판별하는 함수 구현 필요
경우의 수 파악 문제 (탐색) -> 완전 탐색으로 해결 for 문 2번

가장 높은 좌표를 기준으로 그리디하게 확인하면 되는가?

1.일단 경사로를 놓고 활주로 기준으로 거르기
2. 조건이 되면 경사로를 놓고 활주로가 되는지 확인하기

 -> 활주로가 필요한 경우를 모두 찾기 (공중 띄울 수 없어서 그리디하게 풀어봐도 될거 같다.)
 -> 활주로가 중복되어 사용되는지 체크하기

4) 24:09

5) 60:00


"""



sys.stdin = open("4131_sample_input.txt", "r")

# 여기 케이스 찾은건 운이다.
def chechrow_right(h, row, i):
    if i + h < len(row) -1 and (row[i]-1) * h == sum(row[i+1:i+h+1]) and row[i]-1 == min(row[i+1:i+h+1]):
        #if (row[i]-1) * h == sum(row[i+1:i+h]):
        #print(i, (row[i]-1) * h, sum(row[i+1:i+h+1]))
        return tuple(range(i+1,i+h+1))
        
    else:
        return tuple()
def chechrow_left(h, row, i):
    if i - h > 0 and (row[i]-1) * h == sum(row[i-h:i]) and row[i]-1 == min(row[i-h:i]):
        #if (row[i]-1) * h == sum(row[i+1:i+h]):
        #print(i, (row[i]-1) * h, sum(row[i+1:i+h+1]))
        return tuple(range(i-h,i))
        
    else:
        return tuple()


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    #
    count = 0

    # 맵크기 경사로 너비 확인
    n, h = map(int, input().split())
    matrix = list()
    #print(n, h)
    # 리스트로 초기화
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    #print(matrix)

    #print(dir(list))
    
    # 열에 대해 포문으로 확인
    for row in matrix:
        cur_road_list = list()
        #건설할 활주로 좌표 튜플 셋 도출(좌, 우)
        for i in range(len(row)):
            cur_road_list.extend(chechrow_right(h, row, i))
            cur_road_list.extend(chechrow_left(h, row, i))
        #print(cur_road_list)
        #셋으로 합치면서 중복되는 좌표가 있으면 폴스 없으면 트루
        print(cur_road_list, set(cur_road_list))
        cur_i_set = set(cur_road_list)
        if len(cur_road_list) == len(set(cur_road_list)):
            flag = True
            for i in range(n):
                
                if i not in cur_i_set and row[i] != max(row):
                    flag = False
            if flag:
                count += 1

    print(count)
    # 행렬 트랜스포메이션 진행

    # 열에 대해 포문으로 확인
    


#여기서 중단됨

# 패착은 함수가 구현된 기능을 하는지 확인하지 않고 진행한점

# 프린트를 통해 타깃 열을 확인하면 되었는데..!

    
    # ///////////////////////////////////////////////////////////////////////////////////
