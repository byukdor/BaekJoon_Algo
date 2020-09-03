N = int(input())

for i in range(N):
    r, e, c = list(map(int,input().split()))
    if (e - c) == r:
        print("does not matter")
    elif (e - c) > r:
        print("advertise")
    else:
        print("do not advertise")