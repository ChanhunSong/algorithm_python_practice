
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    n , m  = map(int, input().split())
    input_list = [tuple(input()) for _ in range(n)]
    t_list = list()
    pre_list = list()
    #zip이랑 enumerate 같이 쓰면 안됨?
    i = 0
    for item in zip(*input_list):
        pre_list.append("".join(item))
        t_list.append("".join(input_list[i]))
        i +=1
    res =''
    print(t_list, i)
    print(pre_list)
    for i in range(len(t_list)):
        for j in range(len(t_list)-m):
            pass
            
    print("#{}".format(test_case) , res)
