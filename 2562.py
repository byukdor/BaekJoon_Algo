N = 9
numList = []

for i in range(N):
    numList.append(int(input()))

print(max(numList))
print(numList.index(max(numList)) + 1)