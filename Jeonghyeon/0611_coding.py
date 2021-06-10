# 구현
# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 완전 탐색 - 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 시뮬레이션 - 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행


# ✅ 문제
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

# 입력 예시
# 5

# 출력 예시
# 11475

n = int(input())

three = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                 three += 1
            # if '3' in str(j):  # 나는 이걸로 했는디 ㅠㅠ
            #     count += 1
            # if '3' in str(k):
            #     count += 1
print(three)