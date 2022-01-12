def solution(n, lost, reserve):
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
    return answer