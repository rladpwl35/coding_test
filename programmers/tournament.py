
import math
def solution(n,a,b):
    answer = 1

    a,b = sorted([a,b])[0], sorted([a,b])[1]

    while a + 1 != b or a % 2 == 0:
        a = int(math.ceil(a / 2))
        b = int(math.ceil(b / 2))
        answer += 1

    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/12985