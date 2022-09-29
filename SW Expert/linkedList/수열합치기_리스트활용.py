'''
수열이 여러개니까 비교를 각각 해줘야지
수열 2의 첫번째 인덱스와 이전 수열의 원소들 각각 모두 비교
큰 숫자가 없을 경우 맨 뒤에
주어진 m개의 수열 모두 비교해서 정렬해서 역으로 출력
'''

import sys

sys.stdin = open("sample_input.txt", "r")
#테스트케이스
testcase=int(input())
#n,m 비교
for t in range(1,testcase+1):
    n,m=map(int,input().split())
    #첫 리스트 입력받자
    firstlist=list(map(int,input().split()))
    #리스트 입력받았으니까 개수 -1
    for _ in range(m-1):
        #삽입할 수열
        temp=list(map(int,input().split()))
        check=True
        for i in range(len(firstlist)):
            #삽입할 수열의 원소보다 크니?
            if firstlist[i]>temp[0]:
                #슬라이싱 사용할게
                firstlist[i:i]=temp
                #체크변수 변경
                check=False
                #반복문 탈출
                break
        #끝까지 못찾았다면 제일 뒤에 추가
        if check:
            firstlist.extend(temp)

        #역으로 추가해줄게 오케
    #print(firstlist)
    #결과 출력
    print("#{}".format(t), *firstlist[-1:-11:-1])
    
