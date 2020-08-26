x = int(input())
answer = 1
count = 1

while True:
    if x <= answer:
        print(count)
        break
    else:
        count += 1
        answer += (6 * (count - 1))
