a = ("10 10")
b = ("0 30")
c = ("23 40")

a = list(map(int,a.split()))
b = list(map(int,b.split()))
c = list(map(int,c.split()))


hour = a[0]
minute = a[1]

if minute < 45:
    if a[0] == 0:
        a[0] = 23
    else:
        a[0] -= 1
    a[1] = 60 + (minute - 45)
else:
    a[1] -= 45

a[0] = str(a[0])
a[1] = str(a[1])


print(" ".join(a))
