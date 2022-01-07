import math

def solution(n, lost, reserve):
    if(n < math.log(len(reserve), 2)):
        answer = n
        #ü���� Ȯ���� �����ϱ� ���� �迭 ���� �糡�� ��� �߰�
        studentList = [1 for i in range(n+2)]
        #print(studentList)
        for i in reserve:
            studentList[i] += 1
        for i in lost:
            studentList[i] -= 1
        #ü������ ������ �� �ִ��� Ȯ��
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
        #���� �� �� ���� �ο� ����
        reserveSet = reserveSet - lostSet
        #?? �̰� �³� �������δ� �´µ� �� �����ϰ� �ߴ��� ����. ���ǿ����� and ������ ������ ������ ������ ���� �������ְ� for���� ���տ��� sorted�� ����Ѵ�.
        lostSet = lostSet - set(reserve)
        for i in reserveSet:
            if i-1 in lostSet:
                lostSet.remove(i-1)
            elif i+1 in lostSet:
                lostSet.remove(i+1)
        answer = n- len(lostSet)

    return answer
