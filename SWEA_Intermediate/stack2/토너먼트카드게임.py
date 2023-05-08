'''

분할 정복 대표 격이다

 1은 가위, 2는 바위, 3은 보

 비긴 케이스는 고려하지 않겠다. > 있으면 양심 없다. > 놀랍게도 양심이 없다.
 > 하지만 설명에 써놨으니 머쓱하다.

 둘을 빼서 양수 1이면 오른쪽 이김 %2쓰면...?

 둘을 빼서 음수 1이면 왼쪽 이김

하드코딩하면 쉬운데 뭔가 원리가 있을거 같다.

> 음 그냥 dict 써서 자기를 이기는게 아니면 지는걸로 구현해 보겠다.

'''
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())


game_dict = {
    1:2,
    2:3,
    3:1
    }
def win(c_i1, c_i2, card_tuple):
    #print('win',c_i1, c_i2, card_tuple)
    if game_dict[card_tuple[c_i1]] == card_tuple[c_i2]:
        return c_i2
    else:
        return c_i1

def dandc(s,e ,card_tuple):
    #print((s,e ,card_tuple))
    if s==e:
        return s
    if s+1 == e:
        return win(s,e,card_tuple)
    else:
        return(win(dandc(s,(s+e)//2 ,card_tuple), dandc((s+e)//2+1,e ,card_tuple), card_tuple))



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    card_tuple = tuple(map(int,input().split()))
    #print(card_tuple)
    res = dandc(0,n-1 ,card_tuple)
    print("#{} {}".format(test_case,res+1))

    
