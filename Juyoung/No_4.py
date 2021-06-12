'''
공간의 크기를 나타내는 N
A가 이동할 계획서 내용
가 도착할 최종 지점의 좌표

L : 왼쪽으로 한 칸
R : 오른쪽으로 한 칸
U : 위로 한 칸
D : 아래로 한 칸

처음 좌표는 (1, 1)
'''

'''
A = list(str(input()))  ##LLDD

start = [1, 1]


for m in A:
    if m == "L":
        start[0] += 1
    elif m == "R":
        start[0] -= 1
    elif m == "U":
        start[1] -= 1
    elif m == "D":
        start[1] += 1
  

print (start) #[-1, 3] -> 괄호 없애기, -값 안나오게
'''

move = list(str(input()))

a = 1
b = 1

for m in move:
    if m == "R":
        b += 1
    if m == "L":
        if b <= 1:
            pass
        else:
            b -= 1
    if m == "D":
        a += 1
    if m == "U":
        if a <= 1:
            pass
        else:
            a -= 1

print(a, " ",b)
