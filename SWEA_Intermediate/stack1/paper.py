
import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    memo_list = [(0,0)]
    res_list = list()
    while(memo_list):
        cur = memo_list.pop()
        if cur[0] * 10 + cur[1]*20  == n:
            res_list.append((cur[0] , cur[1]))
        elif cur[0] * 10 + cur[1]*20  > n:
            continue
        else:
            #print((cur[0]+1, cur[1]) , (cur[0], cur[1]+1))
            memo_list.append((cur[0]+1, cur[1]))
            memo_list.append((cur[0], cur[1]+1))
    
    #res = len(res_list) > 0인 경우 자연스럽게 추가되어 필요없었다.
    res = 0
    for comb in res_list:
        #print(comb , 2**comb[1])
        #if comb[1]:
        res += 2**comb[1]
    print("#{} {}".format(test_case , res))
