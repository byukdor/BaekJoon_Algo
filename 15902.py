a = int(5)
b = ("1 2 1 1 1")
c = int(4)
d = ("2 1 2 1")

for i in range(c):
    if d[i] > b[i]:        
        if b[i + 1] == 1:
            b[i] = 2
            count += 1
        else:
            b[i] = 1
            b[i + 1] =1
            count += 1
    elif d[i] < b[i]:
        

    

