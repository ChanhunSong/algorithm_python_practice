# start 00 23

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def runBus(k , cur_b , res, station_list):
    #print(k , cur_b , res, station_list)
    # 마지막 두정류장이 남았을때
    if len(station_list)==2:
        if station_list[0] - station_list[1] > cur_b:
            return 0
        else:
            return res
    if station_list[-2] - station_list[-1] > k:
        return 0
    else:
        cur_b = cur_b - (station_list[-2] - station_list[-1])
        if cur_b < 0:
            return 0
        station_list.pop()
        return_num = runBus(k , cur_b , res, station_list)
        if return_num == 0:
            res +=1
            cur_b = k
            return_num = runBus(k , cur_b , res, station_list)
        return return_num
            
    

# DP > 지만 그리디문제
for test_case in range(1, T + 1):
    k , n , m = map(int, input().split())
    #map_list = []*(n+1) > 밑에 리스트로 충분할것 같다.
    station_list = list(map(int , input().split()))
    station_list.append(n) # 도착지 추가
    station_list.reverse()
    station_list.append(0) # 출발지 추가
    # 패딩
    res_num = runBus(k , k , 0, station_list)

    # 모든 원소를 순회 
    print("#{} {}".format(test_case , res_num))
