"""
복잡도는 (m*m) 이나오겠지만 1000개 이하기 때문에 괜찮을거 같다.

break 을 까먹었다.

제한 시간 초과가 떴다. 링크드 리스트를 쓰라는 말이지만 귀찮...

start 41 > 56 실전에서 구현을 할 수 있기에는 어려움이 많다.

deque 을 쓰자! > 어차피 값 확인하는라 꺼내야 하는데 이걸 기점으로 붙여버리자

deque는 연결리스트는 아니였다. extend가 중간에 넣어주질 않는다.

다시 생각해보니 우리는 맨 뒤에 10+n개의 값과 그 앞에 최대값만 기억하고 있으면 된다.

그 이유는 10+n개 이전에 큰값이 있었다면 뒤에 영향 없이 붙었을것이기 때문
> 최대값만 기억하고 있다가 만족하지 않으면 리스트 체크후 변환
"""

import sys

sys.stdin = open("sample_input.txt", "r")

def listSum(input_que , target):
    index = len(input_que)
    for i , v in enumerate(input_que):
        if v > target[0]:
            index = i
            break
    if index == len(input_que):
        input_que = input_que + target
    else:
        input_que = input_que[:i] + target + input_que[i:]
    return input_que


    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_que = (tuple(map(int, input().split())))
    max_num =0
    for _ in range(m-1):
        target= tuple(map(int, input().split()))
        if len(input_que) <= 10 + n:
            input_que = listSum(input_que , target)
        else:
            temp_list = input_que[:len(input_que)-(10+n)]
            input_que = input_que[len(input_que)-(10+n):]
            max_num = max(max(temp_list), max_num)

            t_max = max(target)

            if max_num < t_max:
                input_que = listSum(input_que , target)
        
                 
    print("#{}".format(test_case), *input_que[-1:-11:-1])
