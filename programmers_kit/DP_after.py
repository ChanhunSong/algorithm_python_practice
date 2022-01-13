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
    number_list_set = [set() for i in range(0,9)]
    for i in range(1,len(number_list_set)):
        #처음 연산은 넘어가기
        #if len(item) !=0 :
            
            #연산 시작하기 전에 이전 단계 집합이랑 차집합 - 그러면 없는 조합만 얻어지지 않을까?
            """>> 위에 생각이 잘못되었다는것을 깨닫는데 3시간이 걸렸다. 못 푸는것은 그럴수 있지만
빠르게 생각을 정리하고 새로운 시도를 하기 까지 오래 걸린것이 가장 큰 문제이다.


            """
        for x in range(1,i):    
            for num1 in (number_list_set[x]):
                for num2 in number_list_set[i-x]:
                    if(num2 != 0):        
                        number_list_set[i].add(num1 + num2)
                        number_list_set[i].add(num1 - num2)
                        number_list_set[i].add(num1 * num2) 
                        number_list_set[i].add(num1//num2)
        #붙이기 연산 값 추가 여기에 1은 피해가게 하면 되기는 하는데 너무 하드코딩이라 고민
        number_list_set[i].add((lambda x , y : y*(int('1'*x)))(i, N))
        
        if number in number_list_set[i]:
            print(len(number_list_set[i]))
            answer = i
            break
    return answer

#문제를 해결할 때 지지부진 했던 큰 지분의 이유는 문제를 정확하게 파악하고 단계를 나누지 않아서 많이 해맸다.
#복잡도의 지수가 바뀔정도의 효율성이 아니라면 가독성이 높은 코드를 작성해라
#강의 코드를 참조하지는 않았음
