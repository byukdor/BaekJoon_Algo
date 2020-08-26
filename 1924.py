month, date = list(map(int,input().split()))
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
monthDiff = month - 1
diff = 0

for i in range(1,monthDiff+1):
    if i in [1,3,5,7,8,10]:
        diff += 31
    elif i == 2:
        diff += 28
    else:
        diff += 30

print(day[(diff + date - 1) % 7])