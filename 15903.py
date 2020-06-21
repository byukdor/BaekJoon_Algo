first = ("4 2")
second = ("4 2 3 1")

first = list(map(int,first.split()))
second = list(map(int,second.split()))


for i in range(first[1]):
    minimum1 = min(second)
    second.pop(second.index(min(second)))
    minimum2 = min(second)
    second.pop(second.index(min(second)))
    total = minimum1 + minimum2
    second.extend([total,total])

print(sum(second))

