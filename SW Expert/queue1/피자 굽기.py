import sys

sys.stdin = open("sample_input.txt", "r")

from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n , k = map(int,(input().split()))
    pizza_list = list(map(int , input().split()))
    for i in range(k):
        pizza_list[i] = [pizza_list[i] , i]
    pizza_list.reverse()
    i = 0
    cook_list = list()
    for _ in range(n):
        cook_list.append(pizza_list.pop())
    #print(pizza_list , cook_list)
    i = 0

    while(len(cook_list) >1):

        
        while(cook_list):
            print(i,cook_list, pizza_list)
            cook_list[i][0] = cook_list[i][0]//2
            if cook_list[i][0] == 0:
                cook_list.pop(i)
                break
            i = (i+1)%len(cook_list)
            
        if pizza_list:
            cook_list.append(pizza_list.pop())
        else:
            if i >= len(cook_list):
                i = 0

        
        

    print("#{} {}".format(test_case,  cook_list[0][1]))

