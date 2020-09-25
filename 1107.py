N = int(input())
num_broken = int(input())
broken_list = []
if num_broken == 0:
    pass
else:
    broken_list = list(map(str,input().split()))
possible = []


for i in range(1000001):
    broken = False
    for j in str(i):
        if j in broken_list:
            broken = True
    if not broken:
        possible.append( min(abs(N - 100), abs(N - i) + len(str(i))))

if num_broken != 10:
    print(min(possible))
else:
    print(abs(N - 100))