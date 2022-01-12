def solution(number, k):
    #어떤 문제인지 파악하지 못했을때 처음 문제 풀이를 하려고 했을 때 가장 모든 자리수를 제거하는 경우의 수중에서 가장 큰 수를 선택해 가는 단계를 생각했다. 이것에 대한 복잡도는 n^2이다. 푼 방식은 브루트 포스....
    
    #그리디 알고리즘이라는 것을 알고 입출력의 예를 다시 보았다. 정해져있는 숫자에서 하나씩 빼는 것이고 숫자의 특성상 같은 개수를 뺀다면 맨앞에 가장 큰수를 남기는게 좋다. 
    #근데 이거는 버블 소트를 한번만 돌리는 것과 같은 로직으로 해결할 수 있다. 앞과 뒤를 비교해서 앞이 크면 남기고 뒤가 크면 앞을 제거한다. 
    #자리수가 정해져 있기 때문에 이것보다 커질 수 없다고 생각하고 문제를 푼다.
    #끝까지 가기전에 빼야하는 개수가 정해져 있기 때문에 현재 남은 문자열과 빼야하는 문자열의 값이 같아지면 해당하는 문자열부터 모두 제거하고 리턴
    stringNumber = list(str(number)) 
    answer = ''
    stringNumber.append('0')
    print(stringNumber)
    #2개보다 클때 작동하도록
    if len(stringNumber) > 2:
        for i , num  in enumerate(stringNumber):
            print(len(stringNumber)-(i+2), answer, num ,k)
            if (len(stringNumber)-(i+2)) == k or i+1 == len(stringNumber) : 
                break
            # 뒤에가 크면 버림 > k-1 
            #print(i,num)
            if num < stringNumber[i+1] :
                k -= 1
            # 앞에가 크거나 같으면 살림 > 답에 현재 값 추가
            else:
                answer =   answer + str(num)
                
            
            # 자리수 - (i+1) == k >> 현재 확인해야하는 범위와 제거해야 하는 범위가 같아지면>> 위에 연산이 끝나고 포문을 끝낼지 결정
            """
            
            
            if (len(stringNumber)-(i+2)) == k : 
                break"""
    else:
        answer =  stringNumber
        
    #한개일때 한개일때는 뺄수 없으니 한자리일때 입력값 리턴
    return answer
