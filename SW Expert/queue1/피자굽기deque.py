import sys

sys.stdin = open("sample_input.txt", "r")


from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n , k = map(int,(input().split()))
    pizza_list = list(map(int , input().split()))
    for i in range(len(pizza_list)):
        pizza_list[i] = [pizza_list[i] , i]

    pizza_list.reverse()
    que = deque(list())

    for _ in range(n):
        que.append(pizza_list.pop())

    while(len(que)>1):
        cur = que.popleft()
        cur[0] =  cur[0]//2
        print(cur , que)
        if cur[0] == 0:
            if pizza_list:
                que.append(pizza_list.pop())
        else:
            que.append(cur)

    print("#{} {}".format(test_case , que[0][1]+1))
