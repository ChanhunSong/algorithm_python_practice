import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

h_dict = {
    '0' : "0000", 
    '1' : "0001", 
    '2' : "0010", 
    '3' : "0011", 
    '4' : "0100",
    '5' : "0101",
    '6' : "0110",
    '7' : "0111",
    '8' : "1000",
    '9' : "1001",
    'A' : "1010",
    'B' : "1011",
    'C' : "1100",
    'D' : "1101",
    'E' : "1110",
    'F' : "1111"

}
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
    if len(T_input) > 2 : 
        for item in T_input[2:]:
            res += h_dict[item]
        print('#' + str(test_case) + " " + res)
    else:
        print("0000")
    # ///////////////////////////////////////////////////////////////////////////////////
    
