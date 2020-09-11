N = int(input())
count = 0

for i in range(1,N + 1):
    if i <= 99:
        count += 1
    
    else:
        numChar = list(map(int,str(i)))
        if numChar[0] - numChar[1] == numChar[1] - numChar[2]:
            count += 1

print(count)