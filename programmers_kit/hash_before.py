def solution(participant, completion):
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
    ���⼭ ��ĥ ���� �� 
    1. ����� get , items �Լ� ������� �ڵ� �������� ������ �� ���̸� ����
    https://wikidocs.net/22805
    2. ����Ʈ �������ڼ��� ����Ͽ� �� �� ���̽���ϰ� �ڵ带 «
    https://wikidocs.net/22805
    3. ���ǿ� ����Ʈ��������ǿ��� k for k�� �� ���ΰ�
    ???
    a , b = (0, 2) , (0, 3)
    print(a[0]-b[0],a[1]-b[1])
    """
    return answer
