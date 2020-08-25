N, C = list(map(int,input().split()))
numList = [0] * (C+1)

for i in range(N):
    num = int(input())
    if num == 1:
        numList = [C]
        break
    for i in range(num,C + 1, num):
        if not numList[i]:
            numList[i] = 1

print(sum(numList))