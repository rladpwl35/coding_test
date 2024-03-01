def solution(s):
    s = list(map(int, s.split()))
    answer = str(min(s)) + ' ' + str(max(s))
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/12939