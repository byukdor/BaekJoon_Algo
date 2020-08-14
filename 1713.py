
#a = int(input())
#b = int(input())
#c = list(map(int,c.split()))

a = 3
b = 9
c = "2 1 4 3 5 6 2 7 2"
c = list(map(int,c.split()))

list_ = []
count = []
loca = []
for i in c:
    if len(list_) < a:
        if i in list_:
            count[list_.index(i)] += 1
        else:
            list_.append(i)
            count.append(1)
            loca.append(len(list_)-1)
    else:
        if i in list_:
            count[list_.index(i)] += 1
        else:
            location  = count.index(min(count))
            list_.pop(location)
            list_.append(i)
            loca.pop(location)
            loca.append(location)
            count.pop(location)
            count.append(1)

print(list_)
print(count)
Z = [x for y, x in reversed(sorted(zip(count, list_)))]
print(Z)
print(loca)
