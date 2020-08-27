answer = 0
highest = 0

for i in range(4):
    out, come = list(map(int,input().split()))
    answer += come - out
    if answer > highest:
        highest = answer

print(highest)