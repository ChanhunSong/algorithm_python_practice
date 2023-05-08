'''
전치행렬로 푸는게 빠른가...?


row 맥스 구할때 전치행렬 만들고 맥스값 구하면

100*100 + 100*100

따로 만들어도

100*100

100*100

따로 라이브러리 써서 만들자

대각선 값만 for 문으로 만들어서 처리하


'''


import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    line1= list()
    line2= list()

    matrix = [[] for _ in range(100)]

    for i in range(100):
        matrix[i] = list(map(int , input().split()))

    max_num = 0
    for row in matrix:
        max_num = max(max_num , sum(row))
    for i in range(100):
        line1.append(matrix[i][i])
    max_num = max(max_num , sum(line1))
        
    trans = list()

    for col in zip(*matrix):
        trans.append(col)
        
    for row in trans:
        max_num = max(max_num , sum(row))
    for i in range(100):
        line2.append(trans[i][i])
    max_num = max(max_num , sum(line2))

    print("#{} {}".format(t , max_num))
        
    


    
