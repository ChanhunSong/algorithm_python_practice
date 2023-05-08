import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    score_list = list(map(int, input().split()))
    res_dict = dict()
    for n in score_list:
        res_dict[n] = res_dict.get(n, 0 ) + 1

    answer = 0
    max_num = 0

    for n , res in res_dict.items():
        #print(n,res)
        if max_num < res:
            max_num = res
            answer = n
    print("#{} {}".format(test_case , answer))
