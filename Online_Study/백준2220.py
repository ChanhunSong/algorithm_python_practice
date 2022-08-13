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
    res_list.append(num)
    res_list[-1] , res_list[1] = res_list[1] , res_list[-1]
    return res_list
    

t = int(input())

res = searchMaxSwap(t)

print(*res[1:])
