# No.03 1이 될 때까지

def solution(num,div):
    answer = 0
    
    while num != 1:
        if num % div == 0:
            num = num / div
        else:
            num = num - 1
        answer += 1
        
    return answer

print(solution(25,5))