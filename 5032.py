e, f, c = list(map(int,input().split()))

current = e + f
count = 0

while (current) >= c:
    count += current // c
    current = current % c + current // c

print(count)