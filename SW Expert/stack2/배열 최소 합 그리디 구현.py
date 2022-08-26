'''

세로에서 가장 작은 값이므로

numpy, 전치행렬 두개로 쉽게 풀 수 있을거 같다.

정식 테스트에서 numpy가 허용 안될 수 있으므로 전치행렬로 풀겠다.

?

전치행렬로 초기화가 빠를까
zip이 빠를까..?

아마 zip이 빠를 거 같은데 테스트 ㄱㄱ


그리디

'''
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [[] for _ in range(n)]
    for i in range(n):
        matrix[i] = tuple(map(int, input().split()))
    #tran_matrix = list()
    res = 0
    for row in zip(*matrix):
        print(row , min(row))
        res += min(row)
    print("#{} {}".format(test_case, res))
    
