def solution(N, number):
    #최소값이 8보다 크면 -1을 리턴하므로 주어진 N을 8개의 테이블로 세팅하여 연산에 대한 테이블을 만들면 될거 같다.
    #n * 사칙연산 테이블 생성(-는 잘모르겠는데 사칙연산에 붙이기 연산도 포함해야 한다.)
    #아니면 붙이기 연산을 멱집합으로 만들어서 풀어야 하나 8의 파워셋이면 얼마 안하는거 같기는 함
    #print((3**8+3**7+3**6+3**5)*8) #할만한 크기인데?	52488
    #더하기 연산이 만만하니 더하기 연산을 하고 뒤이어 곱하기 나누기 연산을 해야 하나?
    
    
    #미래의 내가... 위 주석을 보고.. 마이 당황했다... 접근을 잘했지만 동적 계획법을 넣을 부분을 찾지 못했구먼... 
    
    #단계별로 현재의 연산을 구현해보자
    
    # 1 단계 연산 구한다
    # 2
    # 재귀적으로 생각해보면 (이번 단계 이어붙인수) + (이전에 주어진 값들을 모두 더하기 빼기 곱하기 나누기한 값 하면 된다.) 셋을 만든 다음에 현재 찾고 있는 값이 만든 집합에 있는지 확인한다.
    #굳이 재귀함수....? set을 공유해서 연산하면 되니까 그냥 for문으로 구현해보겠다.
    answer = -1
    #숫자 비교를 위한 셋 초기화
    number_set = set()
    for i in range(1,9):
        #처음 연산은 넘어가기
        if len(number_set) !=0 :
            temp_set= set()
            for num1 in number_set:
                for num2 in number_set:
                    temp_set.add(num1 + num2)
                    temp_set.add(num1 - num2)
                    temp_set.add(num1 * num2)
                    if(num2 != 0): 
                        temp_set.add(num1 / num2)
            number_set = temp_set
    #붙이기 연산 값 추가
        number_set.add((lambda x , y : y*(int('1'*x)))(i, N))
        if number in number_set:
            answer = i
            break
    return answer
# 답은 맞지만 효율성 통과를 못함
