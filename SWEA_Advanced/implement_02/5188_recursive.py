"""



재귀 함수로 풀이하기

재귀 + DP

함수 호출 순서가 중요하다.!


아 dp로 숫자(경우의 수)를 개산하는게 의미있는게 아니구먼

경우(상태) 그 자체가 필요한거라 모두 실행되야 의미가 있음

"""

import sys
import itertools
import time

sys.stdin = open("5188_sample_input.txt", "r")

global run_count


"""
def comb(n,r, run_count, dp_list):
    dp_list.append((n,r))
    run_count[0] +=1
    if r == 0:
        #print(tr)
        res.append(tuple(tr[:]))
        if n == 0:
            print("???", tr)


    else:
        tr[r-1] = an[n-1]
        if not n-1 < r-1:
            comb(n-1, r-1, run_count, dp_list)
        if not n-1 < r:
            comb(n-1,r, run_count, dp_list)
"""

def comb(n,r):
    if r == 0:
        pass

    else:
        tr[r-1] = an[n-1]
        if not n-1 < r-1:
            comb(n-1, r-1)
        if not n-1 < r:
            comb(n-1,r)

n = 20
r = 10
run_count = [0]
dp_list = list()

an = [i for i in range(n)]
tr = [0 for _ in range(r)]
res = list()
print(an, tr)
st =  time.time()
comb(n,r)
print(time.time()- st)
#for dp in dp_list:
#    print(dp)

print(" 리프노드의 개수")
print(len(res))
res_set = set(res)
print(len(res_set))

print("재귀함수 총 호출 횟수")

print(run_count)

print("...?")
print(len(dp_list))
dp_list_set = set(dp_list)
print(len(dp_list_set))
st =  time.time()
lib_list = [row for row in itertools.combinations(an, r)]
print("답", len(lib_list))
print(time.time()- st)
