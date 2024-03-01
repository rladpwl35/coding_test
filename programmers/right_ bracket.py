def solution(s):
    answer = True
    op = 0
    clo = 0
    
    for i in s:
        if i == "(":
            op += 1
        else : 
            clo += 1
        if clo > op: 
            answer = False
    if clo != op: 
        answer = False
    return answer
#https://school.programmers.co.kr/learn/courses/30/lessons/12909