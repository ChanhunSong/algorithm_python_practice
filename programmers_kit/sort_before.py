def solution(numbers):
    answer = ''
    #주어진 숫자열을 스트링으로 바꾸어 변환이 쉽게 만들어 준다.(이거 복잡도가???) 
    stringNumbers = [str(k) for k in numbers]
    # 문자열 정렬은 앞자리부터 계산이라 그냥 소트하면 됨 예) 2 , 15 >> 15 , 2 
    stringNumbers = sorted(stringNumbers)
    for string in stringNumbers:       
    # 정렬된 배열을 가지고 뒤에서부터 그냥 이어붙여서 리턴
        answer = string + answer
    
    #두번째 방법으로는 max연산을 통해 리턴된 숫자를 기준으로 자리수를 구해서 나머지 원소에 적용한다. 이거는 복잡도가 n이다.
    return answer
