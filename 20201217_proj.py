'''1 看一個數字是否是質數'''

l = list()
num = int(input("give me your number: "))

if num > 1 :
    for t in range(2 , num-1):
        if num % t == 0:
            print("I'm not prime")
            break
    else:
        l.append(num)
        print("I'm prime")


'''2 以"專案名 參數1 參數2" 在數字1及數字2的範圍找出質數'''

import sys
n = sys.argv

l = list()
num1 = int(n[1])
num2 = int(n[2])

for i in range(num1, num2+1):
    if i > 1:
        for t in range(2, i):
            if i % t == 0:
                break
        else:
            l.append(i)
print(l)









