N = int(input())
case = [0] * (11)
case[1] = 1
case[2] = 2
case[3] = 4

for i in range(N):
    M = int(input())
    for j in range(4,M + 1):
        if case[j] == 0:
            case[j] = case[j - 1] + case[j - 2] +case[j - 3]
    print(case[M])