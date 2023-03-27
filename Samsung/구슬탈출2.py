# 15분 40분에 쉼

"""
투포인터 문제로 보인다.
두개의 객체를 같은 벡터 함수를 통해 좌표를 조정하는 것으로 진행하면 될거 같다.
최단 거리이므로 값을 리턴할때 횟수를 리턴 /

#그래프를 만들고 시작해야 다익스트라 적용가능
#빨간공 결과를 바탕으로 파란색을 탐색하고 구멍에 빠지면 리턴 0

#현재 좌표를 기준으로 방향 조절을 실행하는 함수 구현
#리턴된 결과를 바탕으로 다익스트라

# 그냥 그래프 만들면 편한다.
# 경로상 방향들만 기억했다가 파란색에 적용

# 그래프 좌표와 거리를 저장 / 벡터에 따라 0,1,2,3,

while (벡터함수 실행 횟수):
    

"""


t = int(input())

vectors = ((0,1),(1,0),(0,-1),(-1,0))
def travel(cur, ilist,vectors):
    next_step = [0,0,0,0]
    for i in range(4):
        x, y = cur
        while(ilist


    return next_step
    

for _ in range(t):
    n, m = map(int, input().split())
    ilist = [[]*m for _ in range(n)]
    r_graph = [[[0,0,0,0]]*m for _ in range(n)]
    b_graph = [[[0,0,0,0]]*m for _ in range(n)]
    r = []
    b= []
    o = []

    for i in range(n):
        ilist[i] = list(input())
        for j in range(m):
            if ilist[i][j] == 'R':
                r = (i,j)

            if ilist[i][j] == 'B':
                b = (i,j)

            if ilist[i][j] == 'O':
                o = (i,j)
    tlist = list(r)

    while(tlist):
        cur = tlist.pop()
        next_step = r_graph







    
    
    
