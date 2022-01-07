import math

def solution(n, lost, reserve):
    if(n < math.log(len(reserve), 2)):
        answer = n
        #체육복 확인을 저장하기 위한 배열 생성 양끝에 허수 추가
        studentList = [1 for i in range(n+2)]
        #print(studentList)
        for i in reserve:
            studentList[i] += 1
        for i in lost:
            studentList[i] -= 1
        #체육복을 빌려줄 수 있는지 확인
        for i in range(1,n+1):
            if studentList[i] == 2 and studentList[i-1] == 0:
                studentList[i] = 1
                studentList[i-1] = 1
            elif studentList[i] == 2 and studentList[i+1] == 0:
                studentList[i] = 1
                studentList[i+1] = 1   
        print(studentList)
        for i in range(1,n+1):
            if studentList[i] == 0:
                answer -= 1
    else:
        lostSet = set(sorted(lost))
        reserveSet = set(sorted(reserve))
        #빌려 줄 수 없는 인원 제거
        reserveSet = reserveSet - lostSet
        #?? 이거 맞나 논리적으로는 맞는데 더 간단하게 했던거 같다. 강의에서는 and 연산을 적용한 뺄셈용 집합을 만들어서 연산해주고 for문에 집합에서 sorted를 사용한다.
        lostSet = lostSet - set(reserve)
        for i in reserveSet:
            if i-1 in lostSet:
                lostSet.remove(i-1)
            elif i+1 in lostSet:
                lostSet.remove(i+1)
        answer = n- len(lostSet)

    return answer
