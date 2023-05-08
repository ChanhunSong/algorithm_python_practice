"""
200*1000이면 될거 같은데

최소값 찾는것 100

최대값 찾는것 100

인덱스

다익스트라 써서 풀수 있겠지만 가만히 그리디로 풀어야 겠다.

max 값만 기억하고 있고 가장 작은값에 더해서 넣으면 풀릴까? 안됨

min과 max의 값을 기준으로 딕셔너리+ 리스트로 풀면 될거 같다.



예시에서 상자의 좌표가 맘에 걸리기는 하지만 그리디로 시도해보겠다.

안되네...?

정렬해서 반씩 힙에 넣으면 안되나...? 안되네

이거 그리디로 해결하려면

높이로 정렬

앞 뒤로 빼서 중간에 넣는다. > 링크드 리스트로 해야하네

"""


import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    b_list = list(map(int, input().split()))

    b_dict = dict()
    min_h = min(b_list)
    max_h = max(b_list)
    
    for i, b in enumerate(b_list):
        b_dict[b] = b_dict.get(b, []).append(i)

    while()
