a = ("12 6")
b = ("7 8 10 10 10 10 10 10 10 3 10 10")
c = ("3 2 5 2 4 6")

first = list(map(int,a.split()))
li = list(map(int,b.split()))
pizzas = list(map(int,c.split()))

for i in range(1,first[0]):
    if li[i] > li[i-1]:
        li[i] = li[i-1]

current_height = first[0] - 1

count = 0
for pizza in pizzas:
    if current_height == 0:
        break
    while current_height >= 0 and pizza > li[current_height]:
        current_height -= 1
    
    count += 1
    if count == first[1]:
        current_height += 1
        break
    if current_height > 0:
        current_height -= 1

print(current_height)