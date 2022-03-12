class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        new_index  = len(self.data)-1
        while((len(self.data) > 1) and (new_index > 1) and self.data[new_index//2] < self.data[new_index]):
            self.data[new_index//2] ,self.data[new_index]  = self.data[new_index] ,self.data[new_index//2]
            new_index = new_index//2
        return True
    
    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = i*2

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = i*2+1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data)-1 > left and self.data[left ] > self.data[i]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest  = left 
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data)-1 > right  and self.data[right ] > self.data[i]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest  = right 

        if smallest != i:
            print(i,smallest  ,self.data[i] ,self.data[smallest ])
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[smallest ] ,self.data[i] =  self.data[i], self.data[smallest ]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)


def solution(x):
    return 0
test = MaxHeap()
test.insert(2)
test.insert(3)
test.insert(4)
test.insert(5)
test.insert(1)
print(test.data)
print(test.remove())
print(test.remove())
print(test.remove())
print(test.remove())
print(test.remove())
print(test.remove())

