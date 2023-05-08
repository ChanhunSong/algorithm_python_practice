"""
데자뷰...?????

인덱스를 신경쓰지 않고 하겠다.
"""


import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    res = 0
    n= 100
    input_list = [[]]*100
    res = 0
    for i in range(100):
        input_list[i] = list(input())
    trans = list()
    for row in zip(*input_list):
        trans.append(row)
    while(n>0 and res ==0):    
            
        for row in input_list:
            for i in range(101-n):
                temp = row[i+n//2+n%2:i+n]
                if row[i:i+n//2] == temp[::-1]:
                    print(row[i:i+n//2] ,temp[::-1])
                    #print("re")
                    res = n 
        for row in trans:
            for i in range(101-n):
                #print(row[i:i+n//2] , row[i+n//2+n%2:i+n])
                temp = row[i+n//2+n%2:i+n]
                if row[i:i+n//2] == temp[::-1]:
                    #print("re")
                    res = n
        n -=1
    print("#{} {}".format(test_case , res))
