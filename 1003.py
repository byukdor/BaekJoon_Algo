N = int(input())


for i in range(N):
    M = int(input())
    first = [0] * (M + 1)
    second = [0] * (M + 1)
    for j in range(M + 1):

        if j == 0:
            first[j] = 1
            second[j] = 0
        elif j == 1:
            first[j] = 0
            second[j] = 1
        else:
            first[j] = first[j - 1] + first[j - 2]
            second[j] = second[j - 1] + second[j - 2]

    print(str(first[M]) + " " + str(second[M]))