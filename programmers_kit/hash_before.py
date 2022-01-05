def solution(participant, completion):
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
    여기서 고칠 만한 점 
    1. 딕션의 get , items 함수 사용으로 코드 가독성을 높히고 줄 길이를 줄임
    https://wikidocs.net/22805
    2. 리스트 컨프리핸션을 사용하여 좀 더 파이써닉하게 코드를 짬
    https://wikidocs.net/22805
    3. 강의에 리스트컴프리헨션에서 k for k가 뭔 뜻인가
    ???
    a , b = (0, 2) , (0, 3)
    print(a[0]-b[0],a[1]-b[1])
    """
    return answer
