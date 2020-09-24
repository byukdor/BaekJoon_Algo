alpha_index = [-1] * 26
string = list(input())

for i in range(26):
    if chr(97 + i) in string:
        alpha_index[i] = string.index(chr(97 + i))

print(*alpha_index, sep = " ")