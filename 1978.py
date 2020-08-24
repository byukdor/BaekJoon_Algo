import math
x = int(input())
num = list(map(int, input().split()))
prime = list(range(2,1001))
count = 0

for i in range(2, math.ceil(1000 ** (1/2))):
    for j in prime:
        if j / i == 1:
            pass
        elif j % i == 0:
            prime.remove(j)                   

for k in num:
    if k in prime:                               
        count += 1
print(count)