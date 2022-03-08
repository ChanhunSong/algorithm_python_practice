import itertools
def solution(clothes):
    #위장
    
    answer = 0
    #처음에 딕셔너리를 만들어서 종류별로 뭐가있는지 확인해 보면 안되지.. 딕셔너리는 값이 한개니까

    #경우의 수는 좌표계로 변환하여 계산
    
    #from functools import reduce 공부
    
    clothes_dict = dict()
    for item in clothes:
        if item[1] in clothes_dict:
            clothes_dict[item[1]].append(item[0])
        else:
            clothes_dict[item[1]] = ['empty',item[0]]
    #딕셔너리를 쓰려면 종류로 키를 만들고 값을 더해주는 방식이 맞다
    #넣어줄 때 이미 있는지 확인하는 거는 상수 시간이니까 걸리는 복잡도는 n이다.
    #값을 계산 하는 방식은 개별적인 종류의 개수 +  2차 조합끼리 개수 + 3차 조합 .... 옷의 종류 조합 개수
    #정리하자면 축의 모든 경우의 수 - 원점이 답이다. 모든 좌표값이 답이 되기 떄문
    answer = 1
    #축의 모든 경우의 수
    for i in clothes_dict.items():
        #print(i , len(i[1]))    
        answer *= len(i[1])
    #- 원점    
    answer -= 1
    
    
    return answer    
    
    
    
"""
def solution(clothes):
    answer = 0
    resultList = []
    for i in clothes:
        resultList.append(i[1])
    resultCounter = collections.Counter(resultList)
    keys = list(resultCounter)
    datas = []
    for i in keys:
        datas.append(resultCounter[i])
    print(datas)
    
    #중복 조합으로 구하면 되는데 라이브러리를 잊어버렸습니다.
    for i in range(len(datas)):
        for j in range(len(datas)):
            if (0<=(j-i)) and ((j)<= len(datas)-1):
                temp = 1
                templist = datas[0:j-i] + datas[j:]
                for z in templist:
                    temp = temp*z
                answer = answer + temp
        #answer = answer + i
   """
