from collections import deque


test_list1 = [i for i in range(50000000)]
test_list2 = [i for i in range(50000000)]
import time

start = time.time()
test_list1  = test_list1 +test_list2
print( time.time() -start)


t2= deque(test_list2)
start = time.time()
while(t2):
    t2.popleft()
print( time.time() -start)

start = time.time()
while(test_list1):
    test_list1.pop(0)
print( time.time() -start)



t1= deque(test_list1)
t2= deque(test_list2)

start = time.time()

t1.extend(t2)
#res = list(t1)
print( time.time() - start)


start = time.time()
while(test_list1):
    test_list1.pop(0)
print( time.time() -start)

