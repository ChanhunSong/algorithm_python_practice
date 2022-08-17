import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 방법 1 인접 행렬로 푸는 방법(2차원 배열로) > 구현 쉽고 확인 복잡도 10**2
# 인접 리스트로 푸는 방법 > 구현 ..? 복잡도 확인 복잡도 n

#...? 이러면 뭐가 더 좋은 알고리즘일까..?

#일단 입력으로 받는게 똑같이 n이 걸리기 때문에 복잡도는 같음

# 복잡도가 같다면 구현이 편한게 좋은거 같다. > 이차원 리스트로 품

# 아 결국 범위를 구하려면 논리 연산을 해야하는 데...
# 하드 로직을 공부하기에 좋아보이지만
# 사람이 푸는 부분이 많은건 코테에 적합하지 않은거 같다.


# 행렬로 구현 해서 원소의 값을 전부 바꿔주면
# > 아 여기서 n 안의 값의 영향을 받는구먼
# > 값을 바꿀때 연산이 걸린다.
# > 음... 답을

for test_case in range(1, T + 1):
    n = int(input())
    input_list = list()

    res_list = [ [0]*10 for _ in range(10)]


    for i in range(n):
        input_list.append(list(map(int, input().split())))

    for coor in input_list:
        for i in range(coor[0],coor[2]+1):
            for j in range(coor[1],coor[3]+1):
                #print(i, j ,coor[4] )
                res_list[i][j] += coor[4]
    res_num = 0
    for row in  res_list:
        #print(row)
        res_num += row.count(3)

    print("#{} {}".format(test_case , res_num))





    
    
