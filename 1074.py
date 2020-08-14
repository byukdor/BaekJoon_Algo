N,r,c = list(map(int,input().split()))

r += 1
c += 1

result = 0

for i in range(N,0,-1):
    if r > ((2**i)/2):
        result += ((2**i) ** 2)/2
        r -= ((2**i))/2
    if c > ( (2 ** i) / 2):
        result += ((2**i) ** 2)/4
        c -= ((2**i))/2

print(int(result))
        



