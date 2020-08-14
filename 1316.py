N = int(input())
count = 0

def checker(letter,count):
    unique = set(letter)
    if len(letter) == len(unique):
        return(count + 1)
    else:
        last_character = letter[0]
        for i in range(len(letter)):
            if letter[i] in unique:
                unique.remove((letter[i]))
                last_character = letter[i]
            elif (letter[i] not in unique) & (last_character != letter[i]):
                return(count)
        return(count + 1)

for i in range(N):
    letter = input()
    count = checker(letter,count)

print(count)

