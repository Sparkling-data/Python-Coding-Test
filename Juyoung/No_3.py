
a = int(input('어떠한 수 N: '))
b = int(input('나눌 수 K: '))
count = 0

while a != 1:

    if a%b == 0:
        a = a//b
        # print('나눔')

    else:
        a -= 1
        # print('빼기')
    
    count += 1
        
print(count)
