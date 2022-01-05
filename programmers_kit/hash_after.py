def solution(participant, completion):
    answer = ''
    d = {}
    for i in participant:
        d[i] = d.get(i,0) + 1
    for i in completion:
        d[i] = d[i] - 1
    notFinshMember =  [v[0] for v in d.items() if v[1] > 0 ]
    answer = notFinshMember[0]
    return answer
