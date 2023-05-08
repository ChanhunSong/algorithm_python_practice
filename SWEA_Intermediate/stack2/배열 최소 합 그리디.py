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

def greedy(n, input_matrix, trans_matrix):
    if n == 1:
        return input_matrix[0][0]
    
    greedy_list= list()
    n_set = set()
    for i in range(n):
        n_set = n_set | set(input_matrix[i])
    min_val = min(n_set)
    flag = False
    for i in range(n):
        for j in range(n):
            temp = list() + list(input_matrix[i]) + list(trans_matrix[j])
            temp.sort()
            greedy_list.append((sum(temp)-input_matrix[i][j]*2, temp,(i,j)))
            if temp.count(min_val) ==2 and input_matrix[i][j] == min_val:
                greedy_list = [(sum(temp)-input_matrix[i][j]*2, temp,(i,j))]
                flag = True
                break
        if flag:
            break
    if len(greedy_list) != 1:
        greedy_list = sorted(greedy_list, key = lambda x : x[0]*10 - x[1][0] ,reverse = True)
    x, y = greedy_list[0][2][0], greedy_list[0][2][1]
    print(x, y,greedy_list)
    for row in input_matrix:
        print(*row)
    n = len(input_matrix)-1
    n_matrix = [[] for _ in range(n)]
    for i in range(len(input_matrix)):
        if i==x :
            continue
        for j in range(len(input_matrix)):
            if j== y:
                continue
            if i > x and j > y:
                n_matrix[i-1].append(input_matrix[i][j])
            elif i > x:
                n_matrix[i-1].append(input_matrix[i][j])
            elif j > y:
                n_matrix[i].append(input_matrix[i][j])
            else:
                n_matrix[i].append(input_matrix[i][j])

    n_trans_matrix= list()
    for row in zip(*n_matrix):
        n_trans_matrix.append(row)

    select_num = input_matrix[x][y]
    print("run" , select_num, n_matrix)
    return select_num + greedy(n, n_matrix, n_trans_matrix)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    input_matrix = [[] for _ in range(n)]
    for i in range(n):
        input_matrix[i] = tuple(map(int, input().split()))
    trans_matrix= list()
    for row in zip(*input_matrix):
        trans_matrix.append(row)
    res = greedy(n, input_matrix, trans_matrix)
    
            

    print("#{} {}".format(test_case, res))
    
