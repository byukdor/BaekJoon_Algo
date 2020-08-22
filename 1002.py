X = int(input())

for i in range(X):
    x1, y1, r1, x2, y2, r2  = list(map(int,input().split()))

    center_dist = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** (1/2)

    minr = min(r1,r2)
    maxr = max(r1,r2)

    if (x1 == x2) & (y1 == y2) & (r1 == r2):
        print(-1)
    elif center_dist < maxr:
        if center_dist + minr == maxr:
            print(1)
        elif center_dist + minr > maxr:
            print(2)
        elif center_dist + minr < maxr:
            print(0)
    else:
        if (r2 + r1) > center_dist:
            print(2)
        elif (r2 + r1) == center_dist:
            print(1)
        elif (r2 + r1) < center_dist:
            print(0)
