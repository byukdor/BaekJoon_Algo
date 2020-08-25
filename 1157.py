word = input().lower()
unique = list(set(word))
count =[0] * len(unique)

for i in range(len(word)):
    count[unique.index(word[i])] += 1

if sum([x for x in count if x == max(count)]) != max(count):
    print("?")
else:
    print(unique[count.index(max(count))].upper())