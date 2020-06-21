
for a in range(1,100):
    if (a - 3) >= 5 and (a - 3) % 5 == 0:
        print(((a - 3) // 5) + 1)
    elif (a - 6) >= 5 and (a - 6) % 5 == 0:
        print(((a - 6) // 5) + 2)
    elif (a - 9) >= 5 and (a - 9) % 5 == 0:
        print(((a - 9) // 5) + 3)
    elif (a - 12) >= 5 and (a - 12) % 5 == 0:
        print(((a - 12) // 5) + 4)
    elif (a % 5) == 0:
        print(a // 5)
    elif (a % 3) == 0:
        print(a // 3)
    else:
        print(-1)

