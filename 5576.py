
one = []
two = []
for i in range(10):
    one.append(int(input()))

for i in range(10):
    two.append(int(input()))

one.sort(reverse=True)
two.sort(reverse=True)

print( str(sum(one[:3])) + " " + str(sum(two[:3])))
