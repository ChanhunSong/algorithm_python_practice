def solution(participant, completion):
#완주하지 못한 선수
    
    #소1트 해서 해도 될거 같지만 100000명 이니까 딕트를 쓰겠다
    answer = ''
    
    data = dict()
    #일단 입력
    for i in participant:
        data[i] = 0
    #중복 체크
    for j in participant:
        data[j] = data[j] + 1 
        
    #완주 체크
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
