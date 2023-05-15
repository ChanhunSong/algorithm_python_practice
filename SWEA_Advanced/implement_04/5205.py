"""
퀵소트 구현할 일이 없어서 그냥 라이브러리 사용

혹시 뒤에 필요하면 와서 구현할 예정



"""


import sys

sys.stdin = open("5205_sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    target = list(map(int, input().split()))
    target.sort()

    print("#{} {}".format(test_case, target[n//2]))