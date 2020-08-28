import sys
numList = []

for i in range(int(input())):
    numList.append(int(sys.stdin.readline()))

numList.sort()
for i in numList:
    sys.stdout.write(str(i)+'\n')