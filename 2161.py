numList = list(range(1,int(input()) + 1))
answer = []

for i in range(len(numList)):
    answer.append(numList[0])
    numList.pop(0)

    if len(numList) > 0:
        numList.append(numList[0])
        numList.pop(0)

print(" ".join(map(str,answer)))

