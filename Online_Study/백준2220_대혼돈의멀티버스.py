import heapq

t = [3,2,1 ]

t1 = [3,1,2]

heapq.heapify(t)
heapq.heapify(t1)

print(t, t1)


# start 12

# 처음에 그냥 역 오름 차수 주면 되는 건가 했는데 그건 아니다.

# 재귀적으로 n과 부분집합 문제로 풀면 되나 했는데 입력이 10만이라 안된다.

# 그리디...로 풀릴거 같은데...

# 일단 중복없이 순열을 이루게 되어 남은 부분 집합에서 무조건 swap이 되는 놈이 있다.

# 그럼 단계적으로 스왑이 되게 재귀를 만들면 될거 같다.

# 스왑이 일어나는 조건은 기억에 완전 이진 트리여서 깊이를 기준으로 하나씩 바꾸게 하면 될거 같다.



# heap 영상을 보고 왔다. 접근을 유지하면 될거 같다.

# 한가지 의문인 것은 이게 항상 같은 값이 정답이 되는지 궁금하기는 한데 일단 진행해보겠다.

#스왑을 일을키면서 인덱스를 저장하고 나중에 인덱스에 따라 출력을 넣으면 될거 같다.

#논리 식을 저장하게 하고 싶은 마음이 드는구먼

#마지막까지 스왑이 일어나게하는 조건은 인덱스 0이 인덱스 1보다 작으면 스왑이 일어남

def searchMaxSwap(i_list, step):
    
    if 1 == len(i_list):
        return i_list
    # pop
    i_list[0] ,i_list[-1-step] = i_list[-1-step] ,i_list[0]
    step += 1
    # swap
#루트 노드에 들어올 수 있는 모든 원소의 집합을 구하고
#마지막 루트 노드에 들어올 수 있는 값들을 단계적으로 빼면서 해볼까..?
#마지막에 있는 놈은 마지막에 -1위치  즉 인덱스 1에 존재해야하니까..?

set_list = list()
# 팝 하나는 이미 한다고 가정
for i in range(t,0,-1):
    in_set = set()
    for x in range(i//2):
        in_set.add(x)
    set_list.append(in_set)



> 3은 어케 할라 그러나 했는데 출력은 힙만 허용

> 따라서 3에서 나오는 경우도 1개의 답이 나오네


1

1 2 > 이걸 포함하는경우의 수만 허용
>    
2 1

1 2 3 > 3 2 1 <

1 3 2 > 3 1 2 

2 3 1 > 3 2 1 <

2 1 3 > 3 1 2

3 1 2

4 1 2

4 1 2 3

3 1 2

1 3 4 2 <

1 4 3 2

2 3 4 1

2 4 3 1

1 4 5 2 3

1 4 5 3 2

1 5 4 2 3

1 5 4 3 2



> 재구적으로 이전 단계의 리턴 힙을 가장 뒤에 값이 앞에 오면서 뒤에
>리스트 값을 그냥 붙이고 나서 자신의 단계의 수를 가장 앞에 두면 된다.

> 재귀로... 풀릴 거 같은데... 규칙이 안보인다면... 일단 ... 뒤에서부터 써보자..




t = int(input())

i_list = [i for i in range(t)]

print(i_list)


논리 와 직관! > SW expert A C T> 40 분 1강


직관으로 풀면 박살나는 이유를 몸소 깨닫는 중 > 왜 단계별로 한번의 스왑만 있다 생각했을까

>.? 직관 그차제 , 입력이 n이고... 기본 문제여서...?

5 4 3 2 1

팝

1 4 3 2
스왑
4 1 3 2
스왑
4 2 3 1

팝

1 2 3
스왑
3 2 1

팝
1 2
스왑

2 1

팝


6 5 3 2 4 1
팝

1 3 2 4 5 ....? 뭐지 나는 왜 뒤로 5를 넣었지...???
스왑
3 2 1 4 5
스왑
3 5 1 4 2
스왑
5 3 1 4 2
스왑
5 3 4 1 2

일까..? 아님 

15324
s
51324
s
54321 > 음 합리적으로 전단계가 나오기는 하는군

교환을 해줘야 하기는 했지만  깊이에 따라 해주어야 했구먼

전 단계를 받아서 가장 마지막 원소의 인데스를 파악해서
다음 뎁스의 부모 노드랑 바꾸고 그다음 부모랑 바꾸는 식으로
그리고 마지막에 첫번째 노드랑 마지막 노드 위치 바꾸고 앞에 num 붙인다.




import sys
sys.setrecursionlimit(10**7)

def searchMaxSwap(num):
    
    if 1 == num:
        return [0,1]
    elif 2 == num:
        return [0, 2, 1]
    elif 3 == num:
        return [0, 3, 2, 1]

    res_list = searchMaxSwap(num-1)

    tail_index = len(res_list)-1
    if tail_index > 1:
        while tail_index != 1:
            res_list[tail_index] , res_list[tail_index//2] = res_list[tail_index//2] , res_list[tail_index]
            tail_index = tail_index//2
    return [0] + [num] + res_list[2:] +[res_list[1]]

[0] + [res_list[1]] +  res_list[2:]

    2:
        > n 

t = int(input())

res = searchMaxSwap(t)

print(*res[1:])


인덱스도 틀렸었다.

시간 초과 떴다.

아마 : 문법을 써서 그런듯 하다.
