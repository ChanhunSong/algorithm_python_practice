
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 10개 보다 적은 경우는 없다.
# 하드 코딩으로 구현해도 되겠다.

for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    res_list = list()
    for i in range(5):
        res_list.append(num_list[-1-i])
        res_list.append(num_list[i])
    print("#{}".format(test_case) , *res_list)
