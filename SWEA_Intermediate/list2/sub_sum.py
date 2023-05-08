import sys

sys.stdin = open("sample_input.txt", "r")

import itertools

#T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 12개의 원소중 순서 상관업이 n개를 뽑으니 복잡도는 12 C n 이다.
# 구현은 itertools 쓰면 쉽게할 수 있지만
# 부분 집합을 배웠으니 써먹어 보겠다.
# 안 배웠네..? > advanced에서는 직접 구현해 보겠다.


testcase=int(input())

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
Len=len(arr)

#부분집합 구하기
lst=[]
for i in range(1<<Len):
    sub_lst=[]
    for j in range(Len):
        if i&(1<<j):
            sub_lst.append(arr[j])
        lst.append(sub_lst)

for t in range(1,testcase+1):
    n,k=map(int,input().split())
    #길이 맞는 리스트 구하기
    len_lst=[]
    for i in lst:
        if len(i)==n:
            len_lst.append(i)
    #합 비교
    result=0
    for i in len_lst:
        if sum(i)==k:
            result+=1

    print('#%s %d' % (t, result))
    

