x = input()

answer = int(x)
count = 0

if len(x) == 1:
    x = "0" + x
x = x[1] + str(int(x[0]) + int(x[1]))[-1]
count += 1

while int(x) != answer:
    if len(x) == 1:
        x = "0" + x
    x = x[1] + str(int(x[0]) + int(x[1]))[-1]
    count += 1
print(count)

