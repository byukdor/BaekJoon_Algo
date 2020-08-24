iter = int(input())

for i in range(iter):
    target = list(map(int,input().split()))
    A = target[0]
    target = target[1:]
    mean = sum(target) / A
    print("%.3f%%" % (len([num for num in target if num > mean]) * 100 / A) )
