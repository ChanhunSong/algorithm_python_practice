t = input()
print(t[::-1])
#이미 스트링이 리스트로 형태로 이루어져 있어 뒤에서 부터 출력...

# 스택을 쓰는 방법
t = input()
temp_list = list()
res = ''
for i in t:
    temp_list.append(i)
while temp_list:
    res += temp_list.pop()

print(res)
