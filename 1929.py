import math
M, N = list(map(int,input().split()))

limit = N ** (1/2)
num_list = [1] * (N + 1) 
num_list[1] = 0
start_num = 2

while start_num <= (limit + 1):
    if num_list[start_num]:
        for i in range(start_num * 2, N+1, start_num):
            num_list[i] = 0
        start_num += 1
    else:
        start_num += 1

for j in range(M, N + 1):
    if num_list[j] == 1:
        print(j)