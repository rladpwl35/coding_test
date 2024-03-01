def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    print(A, B)
    for a, b in zip(A, B):
        answer += a * b
    return answer