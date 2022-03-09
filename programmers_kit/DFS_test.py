
import heapq


def solution(tickets):
    answer = []
    #넓이 우선 탐색
    #이 공항과 연결된 공항을 이름순으로 기억하는 힙을 배정?한 리스트 초기화? >> dict
    #이미 방문했는지 결과를 저장하는 set >> 공항은 하나만 있으므로
    com_set = set()
    #우선순위 체크를 위한 이 공항과 연결된 공항을 이름순으로 기억하는 힙을 저장하는 딕트
    tickets_dict = {}
    for x in tickets:
        if x[0] in tickets_dict: 
            heapq.heappush(tickets_dict[x[0]] , x[1]) 
        else:
            # 공항과 연결된 공항을 이름순으로 기억하는 힙을 도착지점을 넣어 초기화
            tickets_dict[x[0]] = [x[1]] 
    
    # ICN부터 출발하기 때문에
    now_airport = "ICN" 
    next_airport = ""
    #answer.append("ICN")
    # 모든 티켓을 사용할때 까지
    while (tickets_dict):
        print(answer)
            # 방문한 곳들을 제외하면 안되네 양방향이라
        #while(tickets_dict[now_airport] and tickets_dict[now_airport][0] in com_set):
        #    heapq.heappop(tickets_dict[now_airport])
        #현재 공항에서 갈 수 있는 곳이 있는지 확인한다.
        if tickets_dict[now_airport]:    
            next_airport= heapq.heappop(tickets_dict[now_airport])
        # 이전 공항을 com_set과 answer에 추가
        
        answer.append(now_airport)
        #딕트의 힙이 비었으면 지우기
        if not tickets_dict[now_airport]:
            del tickets_dict[now_airport]
        #갈 수 있는 공항으로 현재 공항을 바꾼다.
        now_airport = next_airport 

    return answer
"""

import heapq
def solution(tickets):
    #
    #이 공항과 연결된 공항을 이름순으로 기억하는 힙을 배정?한 리스트 초기화? >> dict
    #우선순위 체크를 위한 이 공항과 연결된 공항을 이름순으로 기억하는 힙을 저장하는 딕트
    tickets_dict = {}
    for x in tickets:
        if x[0] in tickets_dict: 
            heapq.heappush(tickets_dict[x[0]] , x[1])
        else:
            # 공항과 연결된 공항을 이름순으로 기억하는 힙을 도착지점을 넣어 초기화
            tickets_dict[x[0]] = [ x[1] ]
    # ICN부터 출발하기 때문에
    now_airport = "ICN"
    next_airport = "ICN"
    # 모든 티켓을 사용할때 까지
    stack = ['ICN']
    path = []
    while(len(stack)> 0):
        print( stack)
        top = stack[-1]
        if top not in tickets_dict or len(tickets_dict[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(tickets_dict[top][0])
            heapq.heappop(tickets_dict[top])
    return path[::-1]

"""

tickets= [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))

print("2단계")

tickets= [["ICN", "BBB"], ["ICN", "AAA"], ["AAA", "ATL"], ["ATL", "ICN"]]
print(solution(tickets))    
  
