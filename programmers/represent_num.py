def solution(n):
    answer = 1
    
    for num in range(1, n // 2 + 1):
        
        sum = 0
        
        while sum <= n:
            sum += num
            
            if sum == n:
                answer += 1
                
            num += 1
            
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/12924