import itertools
def solution(clothes):
    #����
    
    answer = 0
    #ó���� ��ųʸ��� ���� �������� �����ִ��� Ȯ���� ���� �ȵ���.. ��ųʸ��� ���� �Ѱ��ϱ�

    #����� ���� ��ǥ��� ��ȯ�Ͽ� ���
    
    #from functools import reduce ����
    
    clothes_dict = dict()
    for item in clothes:
        if item[1] in clothes_dict:
            clothes_dict[item[1]].append(item[0])
        else:
            clothes_dict[item[1]] = ['empty',item[0]]
    #��ųʸ��� ������ ������ Ű�� ����� ���� �����ִ� ����� �´�
    #�־��� �� �̹� �ִ��� Ȯ���ϴ� �Ŵ� ��� �ð��̴ϱ� �ɸ��� ���⵵�� n�̴�.
    #���� ��� �ϴ� ����� �������� ������ ���� +  2�� ���ճ��� ���� + 3�� ���� .... ���� ���� ���� ����
    #�������ڸ� ���� ��� ����� �� - ������ ���̴�. ��� ��ǥ���� ���� �Ǳ� ����
    answer = 1
    #���� ��� ����� ��
    for i in clothes_dict.items():
        #print(i , len(i[1]))    
        answer *= len(i[1])
    #- ����    
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
    
    #�ߺ� �������� ���ϸ� �Ǵµ� ���̺귯���� �ؾ���Ƚ��ϴ�.
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
