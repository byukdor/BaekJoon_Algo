int(input())

seatList = list(input())

if set(seatList) != {"S"}:
    print(int(seatList.count("L")/2) + seatList.count("S") + 1)
else:
    print(seatList.count("S"))