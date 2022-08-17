import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())


# 이진트리의 뎁스가 어케되는지 물어보는 문제
# 실제 이진 트리를 구현해서 뎁스를 리턴하게 하면되낟.
# 양아치같이 P가 뒤에 두변수 보다 작은 경우는 고려하지 않고 구현하겠다.

def binarySearch(l, r , answer , depth, search_list):
    depth += 1
    mid = int((l+r)/2)
    # 답이 없는 경우는 구현하지 않음 >? 설마 ??? 이거??? 

    #print(l, r , answer , depth)
    if search_list[mid] == answer :#or search_list[l] == answer or search_list[r] == answer:
        return depth
    # 답이 작은 경우
    elif search_list[mid] > answer:
        return binarySearch(l, mid , answer , depth, search_list)
    elif search_list[mid] < answer:
        return binarySearch(mid , r , answer , depth, search_list)

for test_case in range(1, T + 1):
    p , a , b = map(int, input().split())
    # a , b > 1보다 크니까 작은 경우는 고려안함
    # a , b > p 인경우
    # 아니면 끝값 경우에는 답 체크가 안되기는 하는구먼? 아 끝값 맞네
    search_list = [ n for n in range(0, p+1)]
    a_depth = binarySearch(1, p , a , 0, search_list)
    b_depth = binarySearch(1, p , b , 0, search_list)
#a가 짐
    #print(a_depth , b_depth)
    res = 0

    if a_depth > b_depth:
        res = 'B'
    elif a_depth < b_depth:
        res = 'A'
    print("#{} {}".format(test_case , res))

"""
9 9
#1 0
9 6
#2 B
10 10
#3 0

>>>??? 뎁스가 웨케 마이 내려가지
> 끝 값 체크를 안함 > 안하는게 맞음...하핳

2 3
#1 A
9 7
#2 B
8 9
#3 A

> 인덱스 문제 0 패딩
> 인덱스 문제가 맞았는데 전 문제를 해결하기 위한 종료 조건이 문제였다.
> 2번째가 0 이되어야 하는데 그려면 직접 해보자 > 하드 로직으로 할 자신 없다.

테케 2개 못품
> 양아치... 답이 없는 경우는 구현하지 않음 
> 정수라서 범위 안에 있으면 무조건 답이 나옴
> 레인지를 벗어나는 경우..?

1000 299 578

# 아니면 끝값 경우에는 답 체크가 안되기는 하는구먼? 아 끝값 맞네


"""
