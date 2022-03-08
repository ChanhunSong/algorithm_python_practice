# N, K을 공백을 기준으로 구분하여 입력 받기

answer = 0
"""
n, k = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
items = []
for i in range(n):
    item = list(map(int, input().split()))
    #가방에 못넣는거는 제외
    if item[1] <= k and item[1] != 0:
      items.append(item)
    elif item[1] == 0:
      answer += item[0]
"""
n, k = 4,10
items= [[3 ,6 ], [1,2], [2,5], [1,10] ]
#아이템 별로 리스트를 만들어서 단계를 구분한다.
dp_list = [[items[i]] for i in range(len(items)) ] 
result_list = []
#for문 중첩으로 만들면 dp가 아니지
#가치가 높은게 뒤로감
items = sorted(items , key = (lambda x : x[1]))
items = sorted(items , key = (lambda x : x[1]/x[0]  ), reverse = True)
#효율 중심으로 정렬
#무게 무거운 순으로 정렬
#print(items)
while(k > 0 and items):
  #현재 단계에서 이전 단계에 남은 무게를 벗어나지 않는 아이템을 넣는다. 현재 가치를 인덱스 0에 연산후 저장
  best_item = items.pop()
  answer += best_item[0]
  k -= best_item[1]
  while(items and (k < items[-1][1])):
    items.pop()
  #더 이상 이 품목을 대상으로 넣을 수 없다면 최대치라고 판단하여 

  #현재 남은 용량 중에서 넣을 수 있는 값 까지 탐색
  #거기서 용량에 넣고 제거

print(answer)
