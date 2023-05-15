"""

20:00

#...? 제한 시간 초과

bfs써도 되지만 수업 따라 순열로 품



n-1 아래
n-1 오른쪽

중복순열 만들어서 해결 (product)

모든 순열 합 더하여 값 구현

min값 리턴

#...? 


밑에 순열 조합을 이해하기 위한 코드가 있다.

"""



import sys
import itertools
import time

sys.stdin = open("5188_sample_input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    st = time.time()
    n = int(input())
    res = 10**10
    map_list = list()
    for i in range(n):
        map_list.append( tuple(map(int, input().split()))  )

    i_list = (i for i in range((n-1)*2) )
        
    for row in itertools.combinations(i_list, r = n-1):
        x = 0
        y = 0
        cur_sum = 0
        row = set(row)
        """
        cur_sum += map_list[x][y]
        point = 0
        for i in range((n-1)*2):
            if point < len(row) and i == row[point]:
                #print(row, x, point)
                x += 1
                point += 1
            else:
                y += 1
            cur_sum += map_list[x][y]"""
        res = min(cur_sum, res)
    

    print("#{} {}".format(test_case , res))
    print(time.time() - st)
"""
n = 13

test = (i for i in range((n-1)*2) )
num_dict = dict()
count = 0

for row in itertools.combinations(test, r = (n-1)):
    count += 1

    for num in row:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
print(num_dict,count)


test = [i for i in range(6)]
num_dict = dict()
count = 0

for row in itertools.permutations(test, r = 3):
    count += 1
    print(row)
    for num in row:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
print(num_dict,count)
"""

