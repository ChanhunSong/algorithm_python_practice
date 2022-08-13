import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t_num = input() #안씀 하지만 입력 크기를 맞추기 위해 받음
    num_list = list(map(int, input().split()))
#양수가 주어진다고 했으므로
    max_num = 0
#1,000,000 이하 라고 했으므로 가장 작은수 비교를 위한 초기화
    min_num = 10**7
    for num in num_list:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    print("#{} {}".format(test_case ,max_num-min_num))
