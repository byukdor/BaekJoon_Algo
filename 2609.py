X, Y = list(map(int,input().split()))
largest_denominator = 0
smaller = min(X,Y)
larger = max(X,Y)

for i in range(1,smaller + 1):
    if smaller % i == 0:
        if larger % i == 0:
            largest_denominator = i

print(largest_denominator)
print( int((X/largest_denominator * Y/largest_denominator) * largest_denominator))