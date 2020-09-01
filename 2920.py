numList = list(map(int,input().split()))

if numList == sorted(numList):
    print("ascending")
elif numList == sorted(numList, reverse = True):
    print("descending")
else:
    print("mixed")