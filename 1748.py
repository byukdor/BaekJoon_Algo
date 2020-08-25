N = int(input())

length = len(str(N))
answer = 0
for i in range(length):
    if i == 0:
        answer += length * (N - 10 ** (length - 1) + 1)
    else:
        answer += length * (10 ** (length) - 10 ** (length - 1))
    length -= 1

print(answer)