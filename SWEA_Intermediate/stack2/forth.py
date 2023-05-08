
# eval 쓰는 법
'''
정수인걸 어케 구분할까..?

연산자를 체크하는게 쉬울거 같기는 하다.

아마 /연산은 0 체크해야 할거고

일단 사칙연산만 확인


eval > 쓰면 안된다...
'''
import sys


sys.stdin = open("sample_input.txt", "r")

T = int(input())

oper_set = {
    "+",'-','*','/'
    }
for test_case in range(1, T + 1):
    input_list = list(input().split())
    stack = ["error"]
    res = 'error'
    
    for s in input_list:
        print(s, stack, res)
        #. 뒤에도 값이 있는지 체크 ? 의미가 있는지는 모르겠다.
        if s == '.':
            if stack:
                res = stack[-1]
            break
    
        elif s in oper_set:
            #print('run')
            if len(stack) > 2 :
                #print('run')
                n2 = stack.pop()
                n1 = stack.pop()
                if s=="/" and n2 == '0':
                    #res = 'error'
                    break
                snum = 0
                if s =="+":
                    snum = n1 + n2
                if s =="-":
                    snum = n1 - n2
                if s =="*":
                    snum = n1 * n2
                if s =="/":
                    snum = n1 / n2
                stack.append(snum)
            else :
                #res = 'error'
                break
        else:
            stack.append(int(s))

    if len(stack) > 2:
        res = 'error'
    print("#{} {}".format(test_case, res))
