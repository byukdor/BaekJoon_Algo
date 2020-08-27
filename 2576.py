N = 7
numList =[]

for i in range(N):
    num = int(input())
    if num % 2 == 1:
        numList.append(num)

if sum(numList) == 0:
    print(-1)
else:
    print(sum(numList))
    print(min(numList))