def solution(number, k):
    #문제를 다시 풀이해 보았다. 
    #오름차순(같은 값 포함) 이 유지되는 부분으로 수를 리스트로 나누어 K의 수의 따라 수를 크게 만든다.
    #2191에서 k가 1이라면 부분으로 나누는 연산 때문에 1을 지우기는 함 > 나누어 진다는것은 그룹에서 가장 앞에있는 수는 앞선 그룹의 뒷자리 숫자보다는 크니까.
    #3159 에서 k가 2라면 어떨까? >> 이렇게 되면 부분으로 나누는 연산 때문에 정보를 소실한다. 즉 로컬에서 베스트가 아니다.
    #부분으로 나누는것, 오름차순으로 올라가는것은 문제의 본질이 아니다.
    # 이 문제가 나는 그리디 문제라는 것을 알고 있다.
    # 이것을 활용해서 문제를 푼다면 로컬에서 베스트가 전체에서 베스트인 기준을 찾아야 한다는 것이다.
    # 바로 생각 나는 부분은 하나를 뺀 케이스 중에서 가장 큰 수를 선택하는 것이다. 이것의 복잡도는 n제곱이지만 여기서 n은 숫자의 자리수의 해당하기 때문에 7을 넘지 않아 아주 상수적으로 해결이 된다.
    # 처음부터 완벽한 해답은 아닐것이지만 앞선 버전처럼 못푸는 것보다 푼 코드를 개선하는 방향으로 시도해 보겠다.
    
    #숫자를 문자로 만들어 연산을 용이하게 만든다.
    stringNumber = str(number) 
    answer = ''
    # 숫자를 빼는 연산을 반복한다. 주어진 숫자 K의 횟수를 넘지 않는다.
    for i in range(0,k):
        # 될 수 있는 모든 케이스를 만든다. - 현재 스트링리스트에서 하나씩 빼보면서 모든 값을 만든다.
        # 빼는 숫자를 기억하기 위한 변수와 리스트....를 생각했으나 현재 가장 큰수를 다시 stringNumber 변수로 할당하면 될거 같다.
        tempList = []
        for j , item in enumerate(stringNumber):
            if j <= len(stringNumber):
                tempList.append(stringNumber[0:j] + stringNumber[j+1:])
            #else: 파이썬에 미숙해서 추가한 조건 >> 확인 후 주석
            #    tempList.append(stringNumber[0:-1])
            
        
        # 케이스 중에서 가장 큰 수를 선택한다.
        # 숫자를 담는 리스트 
        """
        maxIntList = []
        #리스트에 숫자를 담아주기
        for l in tempList:
            numString = ''
            for num in l:
                numString = numString + num
            maxIntList.append(int(numString))"""
        stringNumber = str(max(tempList))
        
        # 반복문의 마지막이라면 answer에 현재 숫자를 대입한다.
        if i == k -1 :
            answer = stringNumber

    
    return answer
