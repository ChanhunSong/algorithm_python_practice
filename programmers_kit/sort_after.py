def solution(numbers):
    #��Ʈ������ ����� ���ؿ� �´� ���ı��� �ѹ���
    #���� 3�� 3333�� ���� ����ġ�� ������ �ְ� �ڸ����� 4�ڸ��� ���� �����ϱ� ���ϱ� 4 �� �������� �Ѹ� �ȴ�.
    #�� ���� �Լ� �̳� �����ϴ� ������ �迭�� ����� �ʿ���� �������� �ٷ� ������ �ָ鼭 ������ �迭������ �������ش�. ��¥��¥ �����ϴ� �� ������, �ڸ�ǰ����, map,reduce,filter �Լ��鵵 ������
    # sorted �Լ� ���� ������ ������
    # https://offbyone.tistory.com/73 ����, ��
    # https://blockdmask.tistory.com/466 ��Ƽ�� 
    # https://wikidocs.net/22805 ����Ʈ���������
    
    sortedNumbers = sorted([str(x) for x in numbers] , key = (lambda x : x*4 ),  reverse = True)
    if sortedNumbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(sortedNumbers)
    return answer
