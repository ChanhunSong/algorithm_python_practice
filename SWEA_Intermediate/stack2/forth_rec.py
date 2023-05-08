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

def forth(i,input_list, oper_set):
    if i < 0:
        return 'error'
    

    oper = input_list[i]
    print(oper , i)
    if oper in oper_set:
        print("oper run")
        n2 = forth(i-1,input_list, oper_set)
        n1 = forth(i-2,input_list, oper_set)
        snum = 0
        if (n1 == 'error')or (n2 == 'error')or(oper=="/" and n2 == '0'):
            return 'error'
        elif oper =="+":
            snum = n1 + n2
        elif oper =="-":
            snum = n1 - n2
        elif oper =="*":
            snum = n1 * n2
        elif oper =="/":
            snum = n1 / n2
        return snum
    else:
        return int(input_list[i])

for test_case in range(1, T + 1):
    input_list = list(input().split())
    
    res = 'error'
    
    if input_list[-1] != '.':
        res = 'error'
    else:
        res = forth(len(input_list)-2,input_list, oper_set)

    
    print("#{} {}".format(test_case, res))
