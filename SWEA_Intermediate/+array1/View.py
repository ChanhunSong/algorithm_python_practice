"""
255*1000이면 모든 열마다 확인해도 충분하다.

그리디

중앙의 값과 4개의 빙딩중 최대값을 빼서 나온 값이 조망권 개수

이 개수를 더하면 답
"""


import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    h_list = list(map(int, input().split()))
    res= 0

    for i in range(2,n-2):
        temp = h_list[i] - max(h_list[i-2] , h_list[i-1] , h_list[i+1] ,h_list[i+2])
        if temp > 0:
            res += temp
    print("#{} {}".format(test_case , res))
