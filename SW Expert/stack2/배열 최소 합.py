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
    
    #print("#{} {}".format(test_case, res))
    
