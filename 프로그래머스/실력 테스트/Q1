# Q1) 소수판별 
def solution(n):
    answer = 0
    result = []
    for i in range(2,n+1):
        count = 0
        for j in range(2,i+1):
            if i % j == 0:
                count += 1
        if count == 1:
             result.append(i)
    answer = len(result)
    return answer

solution(10)
