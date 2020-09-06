A = 1000 - int(input())
coinList = [500, 100, 50, 10, 5, 1]
count = 0

for i in coinList:
    count += A // i
    A -= (A // i) * i
    if A == 0:
        break

print(count)

