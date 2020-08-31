import sys
N = int(input())
K = N
numList = []
count = 0

for i in range(N):
    numList.append(int(sys.stdin.readline()))

for i in range(N - 1,-1,-1):
    if numList[i] == N:
        N -= 1
        count += 1

print(K - count)