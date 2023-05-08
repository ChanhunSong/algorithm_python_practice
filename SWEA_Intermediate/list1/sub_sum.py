import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    res_list = list()
    for i , item in enumerate(input_list):
        if i + m > n:
            break
        res_list.append(sum(input_list[i:i+m]))
    min_num = min(res_list)
    max_num = max(res_list)
    print("#{} {}".format(test_case , max_num - min_num))
