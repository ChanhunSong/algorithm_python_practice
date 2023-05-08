'''

세로에서 가장 작은 값이므로

numpy, 전치행렬 두개로 쉽게 풀 수 있을거 같다.

정식 테스트에서 numpy가 허용 안될 수 있으므로 전치행렬로 풀겠다.

?

전치행렬로 초기화가 빠를까
zip이 빠를까..?

아마 zip이 빠를 거 같은데 테스트 ㄱㄱ


그리디이지만

이거 퀸 문제였네.. 하핳

복잡도 n**3

부분집합 문제이면서 dp 문제


딕셔너리를 통해 각각 정수에 해당하는 원소에 좌표를 추가한다.

딕셔너리에서 가장 작은 원소부터 부분 집합을 만든다.
(자신의 부분 집합에 겹치는 원소가 없다면 x, y 집합 따로 체크)

재귀적으로 가장작은 원소를 더해가면서 부분 집합을 생성
> 동일한 가중치를 가진다면 모두 후보에 추가

> 답은 나올것이다.

> 브루투 폴스여서 문제다(물론 작은것부터하기에 가지치기는 된거 같다.)
> 더 좋은 방법이 있는가?
> 각 부분 집합마다 이미 고려했던 원소들은 고려하지 않으면 좋을거 같기는 하다
> 이미 이전에 못 넣었다면 지금도 못넣을것
> 가지치기... 음... 최악에 경우에는 어떨까.?
>> 후보에  모든 원소가 같은 경우 후보군에  n**2추가 각각 n**2개 씩 확인 이미 확인한 원소는 확인하지 않으므로
>> n**4... 가 되네..하하

>> n <=10이므로 맞는 접근인거 같다.

아 이거 dfs로 구현...?

일단 답부터 내자


>> 무엇을 풀어야 하는지 모른상태로 접근했다가 깨짐



아... 가로 세로에서 가장 작거나 같은 값을 얻는다면 최적해에 도달하는가?
> 1과 1로 같은 가중치로

11
12

아 같은 1의 가중치를 가져도 베스트 케이스를 가지지는 않는다.

그렇다면 그 선택중 가장 합이 큰 값을 선택한다면 이것은 최적인가?

121
132
143

11143 = 10
12123 = 91

21
32

212 > 5

3 3

답 5



2 1 2
5 8 5
7 2 2

>1
21282 = ?

55
72
>2

5
>5


947
865
537
>3

97
85
>5

9
>9

2+5+9 = 16 (가장 작은 값을 채택하는 것은 틀림)


가장 합이 큰 세로가로합을 선택

947
865
537

>98754 = 33
>94765 = 
>94757
>98655
>98753
>87765 = 33

>>4

85
57
>5
>5

4+5+5 > 14


그리디하게 가장 큰 합 중에서 가장 작은 원소를 찾는 문제로 시도

'''
import sys

sys.stdin = open("sample_input.txt", "r")

import heapq
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [[] for _ in range(n)]
    num_dict = dict()
    for i in range(n):
        matrix[i] = tuple(map(int, input().split()))
        for j, n in enumerate(matrix[i]):
            if n not in num_dict:
                num_dict[n] = [(i,j)]
            else:
                num_dict[n].append((i,j))
    heap = list()

    for n in num_dict:
        heapq.heappush(heap,[n,num_dict[n]])
    start = heapq.heappop(heap)
    stack = list()
    #모든경우를 비교해봐야 하므로 스택
    for i, cor in enumerate(start[1]):
        heapq.heappush(stack , [start[0]+ 0.00000000001*i, [cor] , set(cor[0]) , set(cor[1])])
        #중복 연산이 있음을 알게 되었지만 일단 달린다
    min_num = 10**10
    i = 0
    while(stack):
        cur = heapq.heappop(stack)
        if cur[0] > min_num :
            continue
        if len(cur[1]) == 10 :
            snum = 0
            for cor in cur[1]:
                snum += matrix[cor[0]][cor[1]]
            if min_num > snum:
                min_num = snum
        for 
        # 아 맞다 힙으로 풀때 가중치가 같은면 안되는데...

        i +=1
            

    #print("#{} {}".format(test_case, res))
    
