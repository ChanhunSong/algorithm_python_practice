'''
리턴 값만 가지고 있으면 되잖아...?

이전처럼 영향을 끼치는 범위까지만 연산하고
그 외에는 최대 크기와 현재 인덱스만 체크

>> 생고생이였다.

n 2n ....n*m
가 전문제

n ,n+1 ,,, 2n
가 이번 문제... 음... 복잡도를 계산할 때는 하드로직을 쓸 수 있도록 연습하자
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
        
        
        input_list = numSum(target , input_list)
        
        target = (target+m)
        if target != len(input_list) :
            target = target%(len(input_list))
    print("#{}".format(test_case) , *input_list[-1:-11:-1])




            
