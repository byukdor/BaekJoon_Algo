
a = int(input())
for i in range(a):
    target = list(map(int,input().split()))
    first = int("".join(list(str(target[0]))[::-1]))
    second = int("".join(list(str(target[1]))[::-1]))
    third = first + second
    print(int("".join(list(str(third))[::-1])))




