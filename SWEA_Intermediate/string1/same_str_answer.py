
import sys

import time

sys.stdin = open("sample_input.txt", "r")

start = time.time()
T = int(input())

#..? 짝홀 수 안나누면 전체 확인으로 해도 될거 같기는 한데...

# 0부터 시작하는 m을 m-1하면 어케 되나?

# 9//2 하면 4 나온다.

# 12//2 하면 6나오는데 13개 확인에
# > i =6 일때는 자기 중앙이니까 상관없고자기끼리 비교하니 상관 없을거 같다.

# ...? 그냥 -1 해서 사용하면 된는거네

# 인덱스...? 패딩에 대해 생각해보자

def searchPalindrome(m,string):
    #짝수
    res = ''

    for i, s in enumerate(string):
        #여기까지 왔다면 이게 정답이다.

        if i == m//2+1:
            res = string
            break

        if s != string[-1-i]:
            break

    return res
    

    
for test_case in range(1,  T +1):
    n , m  = map(int, input().split())
    t_list = [input() for _ in range(n)]
    temp = list()
    pre_list = list()
    #zip이랑 enumerate 같이 쓰면 안됨?
    for item in t_list:
        temp.append(tuple(item))
    for item in zip(*temp):
        pre_list.append("".join(item))
    res =''
    half_m = m//2
    #print(t_list , pre_list)
    #print(t_list[0][1+4-1::-1])


    for i in range(n):
        #print(half_m,n-half_m+1)
        for j in range(n-m+1):
            res1 = searchPalindrome(m-1,t_list[i][j:j+m])
            res2 = searchPalindrome(m-1,pre_list[i][j:j+m])
            #print(res1, res2)
            if res1 :
                res = res1
            if res2 :
                res = res2
    print("#{} {}".format(test_case , res))
end = time.time()
print(end - start)
