def solution(n):
    next_n = 1
    while str(bin(n + next_n)).count('1') != str(bin(n)).count('1'):
        next_n += 1
    return n + next_n

#https://school.programmers.co.kr/learn/courses/30/lessons/12911