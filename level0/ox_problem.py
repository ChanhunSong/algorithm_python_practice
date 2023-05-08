def check_pol(x, y, z, op):
    res = ""
    # 더하기
    if op == "+":
        if x+y == z:
            res = "O"
        else:
            res = "X"
    elif op == "-":# 빼기
        if x-y == z:
            res = "O"
        else:
            res = "X"
    return res

def make_test_case(num):
    test_case = list()
    answer = list()

    op_tuple = tuple( ["+" ,  "-"])

    for i in range(-num,num+1):
        for j in range(-num,num+1):
            for z in range(-num*2,(num*2) +1):
                for op in op_tuple:
                    # 테케 추가
                    test_case.append("{} {} {} = {}".format(i,op,j,z))
                    # 답 추가  
                    answer.append(check_pol(i, j, z, op))

                
                    

    return test_case , answer


def check(s):
    res = "O"
    item_list = s.split()
    item_list.reverse()
    num = 0
    while(item_list):
        cur = item_list.pop()
        if cur.isdigit():
            num = int(cur)
        elif cur == "+":
            num += int(item_list.pop())

        elif cur == "-":
            num -= int(item_list.pop())

        elif cur == "=":
            final = int(item_list.pop())
            if num != final:
                res = "X"
    
    return res

def solution(quiz):
    answer = []
    for s in quiz:
        answer.append(check(s))
    return answer

test_case , answer = make_test_case(int(input()))
res = solution(test_case)
print(res == answer)
#for case in test_case:
#    print(case)
wrong_list = list()
for i , ans in enumerate(answer):
    if ans != res[i]:
        print(test_case[i], ans, res[i] )
        wrong_list.append(test_case[i])
print(len(wrong_list))
        
