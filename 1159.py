first_list = []
count_list = []
answer = ''

for i in range(int(input())):
    first = input()[0]
    if first not in first_list:
        first_list.append(first)
        count_list.append(1)
    else:
        count_list[first_list.index(first)] += 1

for i in range(len(count_list)):
    if count_list[i] >= 5:
        answer += first_list[i]

if len(answer) == 0:
    print("PREDAJA")
else:
    print("".join(sorted(answer)))