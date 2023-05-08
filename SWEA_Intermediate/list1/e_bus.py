import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

# DP > 지만 그리디문제
for test_case in range(1, T + 1):
    k , n , m = map(int, input().split())
    #map_list = []*(n+1) > 밑에 리스트로 충분할것 같다.
    station_list = list(map(int , input().split()))
    station_list.append(n) # 도착지 추가
    station_list.reverse()
    station_list.append(0) # 출발지 추가
    # 패딩
    cur_station = 0
    pre_station = 0
    res_num = 0
    for i, station in enumerate(station_list):
        cur_station = station
        print(i, cur_station, pre_station , cur_station - pre_station)
        #다음 정류장 가기전에 베터리가 떨어진다면
        if cur_station - pre_station >k:
            print('run' , station_list[i-1] , pre_station)
            #경우의 수1 내가 건너뛴 경우 , 2 도달하지 못할경우
            if station_list[i-1] == pre_station:#도달 못함
                res_num = 0
                print('?')
                break
            else:
                res_num +=1
                pre_station = station_list[i]
    # 모든 원소를 순회 
    print("#{} {}".format(test_case , res_num))
