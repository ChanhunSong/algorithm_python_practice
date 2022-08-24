arr = [1,2,3,4,5,6,7,8,9,10,11,12]
Len=len(arr)

#부분집합 구하기
lst=set()
for i in range(1<<Len):
    sub_lst=list()
    for j in range(Len):
        if i&(1<<j):
            sub_lst.append(arr[j])
        lst.add(tuple(sub_lst))

print(lst)
