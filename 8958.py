N = int(input())

for i in range(N):
    answer = list(input())
    result = 0
    latest = 0
    for i in range(len(answer)):
        if answer[i] == "O":
            latest += 1
            result += latest
        else:
            latest = 0
    print(result)