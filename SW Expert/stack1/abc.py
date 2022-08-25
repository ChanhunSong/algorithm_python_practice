"""
스택 그자체 문제


"""

import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    string = input()
    # 빈칸 패딩
    stack  = list(" ")
    for s in string:
        if stack[-1] != s:
            stack.append(s)
        else:
            while(stack[-1] == s):
                stack.pop()
    res = len(stack) -1
   
    print("#{} {}".format(test_case , res))
