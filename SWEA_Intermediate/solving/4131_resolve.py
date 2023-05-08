

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


-> 설계 과정은 동일했다...!

- 와 조건 함수를 하나 더 구현하지 말고 데이터를 뒤집는게 시간복잡도 유지 및 안정성 향상
- 셀을 기준으로 계산할때 해당 셀을 시작점으로 포함할 수 있다면 포함하는게 좋다..!
- 일관성을 잃지않고 모듈별로 작동하도록 설계하는게 좋다.



5:03 수정 시작

5:17 일차 수정 -> 안됨 

5:29 문제의 원인은 reverse 했을 때 좌표값의 종속해서 해당좌표 해당 유무를 확인했기 때문에 오류가 났다.

5:31 그냥 2차원 DP 리스트 만들어서 "미사용", "사용", "중복" == 0, 1, 2 로 초기화 해서 확인해 보자

5:35 2차 수정 시작
"""



sys.stdin = open("4131_sample_input.txt", "r")

def checkcorr(w, row, j):
    flag = True
    if  w <= len(row) - j and j-1 >= 0 and row[j-1] == row[j]+1:
        for num in row[j:j+w]:
            if num != row[j]:
                flag = False
    else:
        flag = False
    return flag

# 하나의 기능은 하나의 함수로 구현하자.
def chechrow(w, row, i, j, dp_matrix):
    # 양의 기울기
    if checkcorr(w, row, j):
        for x in range(w):
            dp_matrix[i][j+x] += 1
    #음의 기울기
    row.reverse()
    if checkcorr(w, row, len(row)-1-j):
        for x in range(w):
            dp_matrix[i][j-x] += 1
    row.reverse()
        
        
    


def solve(n, w, matrix):
    dp_matrix = [[0]*n for _ in range(n)]
    count = 0
    #print((n, w, matrix, dp_matrix))
    
    for i, row in enumerate(matrix):
        #print(row)
        
        #건설할 활주로 좌표 튜플 셋 도출(우)
        for j in range(len(row)):
            chechrow(w, row, i, j, dp_matrix)
        print(dp_matrix[i]) 
        # 활주로 조건 확인

        print(row)

        maxnum = max(row)
        flag = True
        for z, state in enumerate(dp_matrix[i]):
            if 
            if state == 0
            #오른쪽 확인

            #뒤집기

            #왼쪽확인
                

            elif state == 2:
                flag = False 
        if flag:
            count += 1
    print(count)
    return count

    
    
T = int(input())
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    #
    

    # 맵크기 경사로 너비 확인
    n, w = map(int, input().split())
    matrix = list()

    dp_matrix = [[0]*n for _ in range(n)  ]
    # 그냥 밑에서 한번더 초기화하는게 안정성이 좋을것 같다.
    dp_col_matrix = [[0]*n for _ in range(n)  ]
    
    # 리스트로 초기화
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    answer = 0
    answer += solve(n, w, matrix)
    """
    # rotate
    rotated_matrix = list()
    for col in zip(*matrix):
        rotated_matrix.append(col)

    

    dp_matrix = [[0]*n for _ in range(n)]
    answer += solve(n, w, rotated_matrix, dp_matrix)

    # 행렬 트랜스포메이션 진행

    # 열에 대해 포문으로 확인
    
    """
    print(answer)



    
    # ///////////////////////////////////////////////////////////////////////////////////
