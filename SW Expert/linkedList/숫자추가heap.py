"""
복잡도는 (m*m) 이나오겠지만 1000개 이하기 때문에 괜찮을거 같다.

break 을 까먹었다.

제한 시간 초과가 떴다. 링크드 리스트를 쓰라는 말이지만 귀찮...

start 41 > 56 완성도 못하고 실행도 못해봤는데 걸렸다.

그냥 논리적으로 해결할 수 있을까?

heap 써써 논리적으로 리스트들을 엮다가 마직막에 한번 합치고 리턴
"""

import sys

sys.stdin = open("sample_input.txt", "r")

import heapq

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # w , list, start
    input_que = [(0,list(map(int, input().split())) , 0 , n)]
    for w in range(m):
        target_list = list(map(int, input().split()))
        index = len(input_que[0])
        flag = True
        while(input_que and flag):
            temp_que = list()
            w , cur , s ,e = heapq.heappop(input_que)
            for i in cur[s:e]:
                if n > target_list[0]:
                    index = i
                    flag = False
                    break
        if index == len(input_list):
            input_list =  input_list + target_list
        else:
            input_list =  input_list[:i] + target_list + input_list[i:]
    print("#{}".format(test_case), *input_list[-1:-11:-1])
    
