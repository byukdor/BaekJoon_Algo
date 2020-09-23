import math
string = input()
length = math.ceil(len(string) / 10)

for i in range(length):
    print(string[i * 10:(i * 10) + 10])