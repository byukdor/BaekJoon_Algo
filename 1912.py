a = "10"
b = "10 -4 3 1 5 6 -35 12 21 -1"

a_2 = "10"
b_2 = "2 1 -4 3 4 -4 6 5 -5 1"

a_3 = "5"
b_3 = "-1 -2 -3 -4 -5"


a = list(map(int,a.split()))
b = list(map(int,b.split()))
#b = list(map(int,b_2.split()))
#b = list(map(int,b_3.split()))

current_sum = 0
last_sum = 0
neg_count = 0

for i in range(len(b)):
    if b[i] >= 0:
        current_sum += b[i]
    else:
        last_sum = max(current_sum,last_sum)
        if current_sum < abs(b[i]):
            current_sum = 0
        else:
            current_sum += b[i]
        neg_count += 1

if neg_count == a[0]:
    print(max(b))
else:
    print(last_sum)




