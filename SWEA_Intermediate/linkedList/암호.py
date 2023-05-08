'''
리턴 값만 가지고 있으면 되잖아...?

이전처럼 영향을 끼치는 범위까지만 연산하고
그 외에는 최대 크기와 현재 인덱스만 체크


'''

import sys


sys.stdin = open("sample_input.txt", "r")


def numSum(target , input_list):
    #target = (i*m)%len(input_list)
    if target == len(input_list):
        input_list = input_list + [input_list[0]+ input_list[-1]]
    else:
        input_list = input_list[:target] +[input_list[target-1]+input_list[target]] + input_list[target:]
    return input_list

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n , m , k = map(int, input().split())
    input_list = list(map(int, input().split()))
    b = 0
    target =m
    for i in range(k):
        #print(input_list)
        if len(input_list) <= 10 + m and b == 0:
            input_list = numSum(target , input_list)
        else:
            print(b , len(input_list))
            temp= len(input_list[:len(input_list)-(10 + m)-1])
            input_list = input_list[len(input_list)-(10 + m)-1:]
            b += temp

            print(temp , len(input_list), b)

            if target > b:
                input_list = numSum(target - b , input_list)
        target = (target+m)
        if target != len(input_list)+b :
            target = target%(len(input_list)+b)
    print("#{}".format(test_case) , *input_list[-1:-11:-1])




            
