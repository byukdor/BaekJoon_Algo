a = ("6 8 10")
b = ("25 52 60")
c = ("5 12 13")
d = ("0 0 0")

while True:
    a = list(map(int,input().split()))
    if min(a) == 0:
        break
    squared = [i**2 for i in a]
    if sum(squared) == 2*max(squared):
        print("right")
    else:
        print("wrong")

