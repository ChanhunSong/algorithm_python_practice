import sys

sys.stdin = open("sample_input.txt", "r")

import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 12개의 원소중 순서 상관업이 n개를 뽑으니 복잡도는 12 C n 이다.
# 구현은 itertools 쓰면 쉽게할 수 있지만
# 부분 집합을 배웠으니 써먹어 보겠다.
# 안 배웠네..? > advanced에서는 직접 구현해 보겠다.


for test_case in range(1, T + 1):
    res = 0
    n, k = map(int, input().split())
    num_list = [ i for i in range(1,12+1)]

    com_list = list(itertools.combinations(num_list, r = n))
    #print(com_list)

    for com in com_list:
        s_num = 0

        for i in com:
            #print(i)
            s_num += num_list[i-1]
        #print(s_num , k)

        if s_num == k:
            res +=1
            
    print("#{} {}".format(test_case ,res))


    #테스트 케이스 6개만 맞음
    # > 문제를 잘 보자 개수를 출력하라 했다. 참거짓으로 자체 필터링 했다.
    

