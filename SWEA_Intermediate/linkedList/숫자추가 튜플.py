"""
복잡도는 (m*m) 이나오겠지만 1000개 이하기 때문에 괜찮을거 같다.

break 을 까먹었다.

제한 시간 초과가 떴다. 링크드 리스트를 쓰라는 말이지만 귀찮...

start 41

deque 을 쓰자! > 어차피 값 확인하는라 꺼내야 하는데 이걸 기점으로 붙여버리자
"""

import sys

sys.stdin = open("sample_input.txt", "r")


from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_que = deque(tuple(map(int, input().split())))
    for _ in range(m-1):
        target_list = deque(tuple(map(int, input().split())))
        temp_que = deque()
        while(input_que):
            if input_que[0] > target_list[0]:
                temp_que.extend(target_list)
                temp_que.extend(input_que)
                input_que = temp_que
                break
            cur = input_que.popleft()
            temp_que.append(cur)
        else:
            temp_que.extend(target_list)
            input_que = temp_que
    input_list = list(input_que)        
    print("#{}".format(test_case), *input_list[-1:-11:-1])
    
