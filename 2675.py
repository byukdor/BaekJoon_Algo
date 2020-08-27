
for i in range(int(input())):
    answer = ""
    num, character = list(input().split())
    character = list(character)

    for i in range(len(character)):
        answer += character[i] * int(num)
    
    print(answer)