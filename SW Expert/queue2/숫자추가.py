"""
복잡도는 (m*m) 이나오겠지만 1000개 이하기 때문에 괜찮을거 같다.

break 을 까먹었다.

제한 시간 초과가 떴다. 링크드 리스트를 쓰라는 말이지만 귀찮...

start 41
"""

import sys

sys.stdin = open("sample_input.txt", "r")

class node:
    def __init__(self, v, i):
        self.i = i
        self.v = v

class linkedList:

    def __init__(self):
        self.end = (None, None)
        self.start = node(None, self.end)
        self.l = 0
    def length(self):
        return self.l

    def seachIndex(self, v):
        cur = self.start
        i = -1
        while (cur != self.end):
            if cur.v == v:
                return i
            else:
                cur = cur.i
            i += 1
    def append(self, v , target):
        cur = self.seachIndex(v)
        new_node = node(cur.i, target)
        cur.i = new_node
        


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    for _ in range(m-1):
        target_list = list(map(int, input().split()))
        index = len(input_list)
        for i , n in enumerate(input_list):
            if n > target_list[0]:
                index = i
                break
        if index == len(input_list):
            input_list =  input_list + target_list
        else:
            input_list =  input_list[:i] + target_list + input_list[i:]
    print("#{}".format(test_case), *input_list[-1:-11:-1])
    
