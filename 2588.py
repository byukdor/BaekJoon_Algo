N = 3
x = int(input())
y = list(input())

for i in range(N, 0, -1):
    print(x * int(y[i - 1]))
print(x * int("".join(y)))