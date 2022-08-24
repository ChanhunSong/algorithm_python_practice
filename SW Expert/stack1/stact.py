# 괄호 검사
"""
4가지 경우
 - 일치
 - 다른 경우
 - 남는 경우
 - 모자란 경우 

"""

import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())

t_dic = {
    "{" : "}",
    "(" : ")",
    "[" : "]"
    }

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_string = input
