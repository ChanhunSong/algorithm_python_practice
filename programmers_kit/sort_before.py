def solution(numbers):
    answer = ''
    #�־��� ���ڿ��� ��Ʈ������ �ٲپ� ��ȯ�� ���� ����� �ش�.(�̰� ���⵵��???) 
    stringNumbers = [str(k) for k in numbers]
    # ���ڿ� ������ ���ڸ����� ����̶� �׳� ��Ʈ�ϸ� �� ��) 2 , 15 >> 15 , 2 
    stringNumbers = sorted(stringNumbers)
    for string in stringNumbers:       
    # ���ĵ� �迭�� ������ �ڿ������� �׳� �̾�ٿ��� ����
        answer = string + answer
    
    #�ι�° ������δ� max������ ���� ���ϵ� ���ڸ� �������� �ڸ����� ���ؼ� ������ ���ҿ� �����Ѵ�. �̰Ŵ� ���⵵�� n�̴�.
    return answer
