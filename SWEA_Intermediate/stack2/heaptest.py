import heapq

heap = list()
for i in range(5, -1,-1):
    heapq.heappush(heap,(i%2, i))

while heap:
    print(heapq.heappop(heap))


heap = list()
for i in range(5):
    heapq.heappush(heap,(i%2, [i]))

while heap:
    print(heapq.heappop(heap))
