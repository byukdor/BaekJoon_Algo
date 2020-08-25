import math
N, K, L = list(map(int,input().split()))

count = 1
trigger = 1

while trigger:
    if math.ceil(K / 2) == math.ceil(L / 2) :
       print(count)
       trigger = 0
    else:
        K = math.ceil(K / 2)
        L = math.ceil(L / 2)
        count +=1