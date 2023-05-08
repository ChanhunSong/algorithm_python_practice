import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_list = [0]*10
    N = input()
    input_list = input()

    for i in input_list:
        num_list[int(i)] += 1
    res_num  = 0
    res_i = 0
    for i , obj in enumerate(num_list):
        if obj >= res_num :
            res_num = obj
            res_i = i
    print("#{} {} {}".format(test_case , res_i , res_num))
