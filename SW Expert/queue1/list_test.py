import time

test = list(range(10000000))
start = time.time()
while(test):
    test.pop()
print(time.time() - start)

test = list(range(10000000))
start = time.time()
while(test):
    test.pop(0)
print("pop test" , time.time() - start)

test = list(range(100000))
start = time.time()
for i in range(len(test)):
    test[i]
print(time.time() - start)

test = list(range(100000))
start = time.time()
for i in (test):
    i = i
print(time.time() - start)

