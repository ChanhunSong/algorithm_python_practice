
import sys


'''
문제분석

1. 문제 유형 시뮬레이션

2. 요구사항

자료구조 선택

1. 연산해야하는 정보는
    1) 시간
    2) 셀 활상태
    3) 셀 가중치
죽은 셀인지 비교를 위한 set이 필요? ㅇㅇ

순서가 필요한가?
ㄴㄴ

시간 은 반복문으로 더하기

시간 + X로 초기화 하기

가중치 더하기


상태 :리스트

죽은 상태를 위한 set 지정


딕셔너리

죽

활

비


함수

활성화 함수(셀,시간 )
    시간과 비교후 활인지 대기인지 구분

활성화 번식 함수(셀, 활, 죽, 비)

업데이트 함수 (메인) (활, 죽, 비, 시간)
    활성화 함수(활셀)
        타겟 확인
    활에서 타겟 빼고 
        활성화 번식 함수
        죽으로 넣기

활성화랑 번식이랑 독립련수여서 순서는 상관없을 듯


1회차 풀이

2 2 10
{(0, 0): [0, 1], (0, 1): [0, 1], (1, 1): [0, 2]}
1026
5 5 19
{(0, 0): [0, 3], (0, 1): [0, 2], (0, 3): [0, 3], (1, 1): [0, 3], (3, 2): [0, 1], (4, 4): [0, 2]}
1310721
9 10 37
{(0, 8): [0, 3], (1, 8): [0, 5], (1, 9): [0, 3], (2, 2): [0, 2], (2, 7): [0, 4], (3, 0): [0, 3], (3, 6): [0, 4], (4, 5): [0, 3], (4, 6): [0, 5], (4, 9): [0, 2], (5, 9): [0, 5], (6, 8): [0, 2], (6, 9): [0, 3], (8, 2): [0, 2], (8, 3): [0, 2]}


'''
sys.stdin = open("5653_sample_input.txt", "r")

#활성화 함수(셀,시간 )
#    시간과 비교후 활인지 대기인지 구분
def check_live(cur_time, cell):
    if cell[0] + cell[1] == cur_time:
        return True
    else:
        return False


vectors = ( (1,0), (-1,0), (0,1), (0,-1))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, k = map(int, input().split())
    dead_cells = dict()
    pre_cells = dict()
    live_cells = dict()
    
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] != 0:
                pre_cells[(i,j)] = [0, row[j]]
    #print(n, m, k)
    #print(pre_cells)

    for time in range(1, k+1 ):

        cur_live_cell = list()
        cur_dead_cell = list()
        
        #활성화 함수(활셀)


            #타겟 확인
        for cell_corr in list(pre_cells.keys()):
            if check_live(time, pre_cells[cell_corr]):
                cur_live_cell.append(cell_corr)


        #활에서 타겟 빼고 
            #활성화 번식 함수
            #죽으로 넣기
        cur_target_live_cells = list(live_cells.items())
        #print(time, cur_target_live_cells)
        cur_target_live_cells.sort(key = lambda x : x[1][1], reverse = True)
        cur_target_live_cell_corrs = [x[0] for x in cur_target_live_cells]
        #print(cur_target_live_cell_corrs)
        for cell_corr in cur_target_live_cell_corrs:
            for vector in vectors:
                cur_new_corr = (cell_corr[0] + vector[0], cell_corr[1] + vector[1])
                if cur_new_corr not in dead_cells and cur_new_corr not in pre_cells and cur_new_corr not in live_cells:
                    pre_cells[cur_new_corr] = [time, live_cells[cell_corr][1]]
            #죽으로 넣기
            if live_cells[cell_corr][0] + live_cells[cell_corr][1] == time:
                cur_dead_cell.append(cell_corr)


        #현시간 셀 죽이기
        for cell_corr in cur_dead_cell:
            dead_cells[cell_corr] = [live_cells[cell_corr][0], live_cells[cell_corr][1]]
            del live_cells[cell_corr]
            
        #현시간 부로 셀 활성화
        for cell_corr in cur_live_cell:
            live_cells[cell_corr] = [time, pre_cells[cell_corr][1]]
            
            del pre_cells[cell_corr]
        

        #print(time, pre_cells)
        #print(time, live_cells)
        #print(dead_cells)

        

        


    
    print("#{} {}".format(test_case , len(pre_cells) + len(live_cells)))

    #문제를 찾는데 50분 걸림 -> 문제를 명확히 이해하는데... 46분 걸림
    # 수정 자체는 빨리 됨..!
    
    # ///////////////////////////////////////////////////////////////////////////////////
