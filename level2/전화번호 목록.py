def solution(phone_book):
    # 문제는 적어도 nlogn의 복잡도를 요구한다.>> 1,000,000은 그냥 n이다.
    # 원소의 길이는 1이상이므로 비어있는 값에 대해서는 생각하지 않아도 됨
    # 중복이 없으니 집합을 사용할 필요가 없다.
    
    # 직관적으로 생각난 방법은 리스트를 정렬하여 자리수 별로 더 큰 자리수를 검사하는 것 >> 이것만 해도 이미 복잡도가 n^2임
    
    # 해시 문제 이므로 해시로 생각해보자 딕셔너리 구조를 사용해서 앞의 접두어로 검색이 되는지 알아보는 기능이 있나?
    # 검색했을 때 안나온다.
    # 자리수를 기억해서 작은 자리수부터 확인해 보는 것이다. 최악의 경우 복잡도는 n / 20(가질수 있는 단계) *20^2 /2(등차수열 )이므로 10 * n의 복잡도를 가진다.
    #n-1 , n-2 , n-3 ... n -20 = 20n - 21*10 >  상수 무시 20n...? 할만 한데? 복잡도는 n이니까
    #종합적으로 복잡도는 리스트 정렬에 걸리는 nlogn이다.
    answer = True
    
    #주어진 리스트를 정렬한다. >> 효율성 테스트 통과 못하는거 봐서 이거 쓰면 안된다. 
    #sorted(phone_book)
    
    
    #주어진 리스트를 작은 순서, 작은 자리수부터 딕셔너리에 담는다.
    #??? 예를 초기화 할때 가장 앞에 있는 원소의 길이로 하면 예외처리를 안해도 된다.
    #run_number_size_set = set()
    #원소를 담을 딕셔너리, 리스트
    number_list = [set() for i in range(0,21)]
    for i in phone_book:
        number_list[len(i)].add(i)
    #print(number_list)
    number_dict = dict()
    for i, num_s in enumerate(number_list):
        for j in num_s:
            for z in range(1,i):
                #print(i , num_s , j , z)
                if j[:z] in number_list[z]:
                    answer = False
        
        #여기에 포문으로 자기 자리수보다 작은 자리수 셋에 접두사가 있는지 조회
        
    return answer   
"""
        #현재 원소의 자리수를 확인한다.
        if len(item) == run_number_size :
            #원소의 크기가 현재 사이즈라면 열심히 딕트에 담는다.
            number_dict[item] = True
        else: 
            #원소의 크기가 현재 사이즈보다 여기부터 뒤까지 잘라서 확인해 본다.
            for test_number in phone_book[i:]:
                if test_number[:run_number_size] in number_dict:
                    answer = False
            #run_number_size를 늘려서 불필요한 계산을 방지한다. >> 이전 코드의 잔재
            #run_number_size = len(item)
    #자리수가 달라지는 지점에서부터 리스트의 끝부분까지 현재 자리수로 잘라서 딕셔너리로 조회되는지 확인한다.
    #조회가 된다면 answer = false로 지정한다.
    
