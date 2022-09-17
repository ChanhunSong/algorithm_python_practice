"""
데자뷰...?????

인덱스를 신경쓰지 않고 하겠다.
"""


import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    #n -= 1
    input_list = [[]]*8
    res = 0
    for i in range(8):
        input_list[i] = list(input())
    trans = list()
    for row in zip(*input_list):
        trans.append(row)
        
    for row in input_list:
        for i in range(9-n):
            #print(row[i:i+n//2] , row[i+n//2+n%2:i+n])
            temp = row[i+n//2+n%2:i+n]
            if row[i:i+n//2] == temp[::-1]:
                #print("re")
                res += 1
    for row in trans:
        for i in range(9-n):
            #print(row[i:i+n//2] , row[i+n//2+n%2:i+n])
            temp = row[i+n//2+n%2:i+n]
            if row[i:i+n//2] == temp[::-1]:
                #print("re")
                res += 1
    print("#{} {}".format(test_case , res))
