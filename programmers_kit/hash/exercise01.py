def solution(participant, completion):
#�������� ���� ����
    
    #��1Ʈ �ؼ� �ص� �ɰ� ������ 100000�� �̴ϱ� ��Ʈ�� ���ڴ�
    answer = ''
    
    data = dict()
    #�ϴ� �Է�
    for i in participant:
        data[i] = 0
    #�ߺ� üũ
    for j in participant:
        data[j] = data[j] + 1 
        
    #���� üũ
    for k in completion:
        data[k] = data[k] - 1
        
    keyList = data.keys()

    
    temp = 0
    for i in keyList:
        if data[i] == 1:
            answer = i
    """
    a , b = (0, 2) , (0, 3)
    print(a[0]-b[0],a[1]-b[1])
    """
    return answer
