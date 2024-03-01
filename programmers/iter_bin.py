def solution(s):
    count = 0
    repz  = 0
    #1일때 까지 반복
    while s != '1':
        count += 1
        
        #0으로 변환하고 변환 수 세기
        for i in range(len(s)):
            if s[i] == '0':
                repz += 1
                
        s = s.replace('0', '')
        
        length = len(s)
        
        # 이진 변환
        bin = ''
        while length > 0:
            bin += str(length % 2)
            length = length // 2
        s = bin[::-1]
                       
    answer = [count, repz]
                       
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/70129