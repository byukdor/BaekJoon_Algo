import math
N = int(input())
A = list(map(int,input().split()))
B, C = list(map(int,input().split()))
count = 0

for i in range(N):
    if A[i] <= B:
        count += 1
    else:
        count += 1 + math.ceil((A[i] - B) / C)

print(count)
