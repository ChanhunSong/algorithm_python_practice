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
    "}" : "{",
    ")" : "(",
    "]" : "["
    }
t_set = {
    "{",
    "[",
    "("

    }

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_string = input()
    stack = [0]
    res = 1
    for s in input_string:
        #print(stack)
        #if len(stack) == 0:
        #    res = 0
        #    break
        if s in t_set:
            stack.append(s)
        elif s in t_dic:
            cur = stack.pop()
            #일치 안하면 , 모자란 경우도 포함
            if cur != t_dic[s]:
                res = 0
                break

                
    if len(stack) > 1:
        res = 0
    print("#{} {}".format(test_case , res))
