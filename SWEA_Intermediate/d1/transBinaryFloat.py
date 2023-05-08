import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def transBinaryFloat(num, res):
    if len(res) > 13:
        return "overflow"
    if num == 0:
        return res
    num = num*2
    print(num)
    if num >= 1:
        return transBinaryFloat(num-1, res+"1")
    else:
        return transBinaryFloat(num, res+"0")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

       1. 재귀로 구현해서 인풋을 디바이드 앤 퀀커로 해결 > 머지소트 처럼 > nlogn 이라 탈락
       2. 각 자리수를 16진수로 바꿔서 각 자리마다 연산 > 변환하는 연산 O(1) * n
       3. 딕셔너리로 16진수 표 만들어서 넣어놓고 각 자리마다 더하기 > 셋에서 가져오는 연산 O(1) * n
       
       시간복잡도 상으로는 2,3 이 같다. > 그래도 연산량이 줄어드는 3이 더 빠르긴 할거 같다.
       
       > 귀찮아서 하드코딩 했는데 이래도 되나...

    '''
    T_input = input()
    res = ""
    print(float(T_input))
    print('#' + str(test_case) + " " + transBinaryFloat(float(T_input), res))

    # ///////////////////////////////////////////////////////////////////////////////////
    
