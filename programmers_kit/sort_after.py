def solution(numbers):
    #스트링으로 만들고 기준에 맞는 정렬까지 한번에
    #기준 3은 3333과 같은 가중치를 가지고 있고 자리수는 4자리를 넘지 않으니까 곱하기 4 한 기준으로 한면 된다.
    #와 람다 함수 겁나 유용하다 원래의 배열을 기억할 필요없이 기준으로 바로 정렬해 주면서 원래의 배열값으로 정렬해준다. 진짜진짜 유용하니 꼭 익히기, 자매품으로, map,reduce,filter 함수들도 익히자
    # sorted 함수 람다 사용법도 익히기
    # https://offbyone.tistory.com/73 람다, 맵
    # https://blockdmask.tistory.com/466 소티드 
    # https://wikidocs.net/22805 리스트컴프리헨션
    
    sortedNumbers = sorted([str(x) for x in numbers] , key = (lambda x : x*4 ),  reverse = True)
    if sortedNumbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(sortedNumbers)
    return answer
