import collections
numList = collections.deque(range(1,int(input()) + 1))

while len(numList) != 1:
    numList.popleft()
    numList.rotate(-1)

print(numList[0])