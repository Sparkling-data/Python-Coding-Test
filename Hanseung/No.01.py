# No.1 큰 수의 법칙

a = [5,8,3] # (n개의 자연수,더할 숫자의 갯수,최대 반복수)
b = [2,4,5,4,6]

def solution(i,v):
    answer = 0
    m = i[1]
    k = i[2]
    v.sort(reverse=True) # 내림차순 정렬

    if v[0] == v[1]: # 가장 큰 수가 두 개인 경우, 더할 숫자의 갯수를 가장 큰 수에 곱함
        answer = m * v[0]
    else: 
        answer = ((k * v[0] + v[1])*(m // (k+1))) + ((m % (k+1)) * v[0])
        
    return answer

print(solution(a,b))