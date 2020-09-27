
def inclusion(x1,y1,cx,cy,r):
    dist = ((cx - x1) ** 2 + (cy - y1) ** 2) ** .5
    if dist <= r:
        return True
    else:
        return False

N = int(input())
for i in range(N):
    x_start, y_start, x_end, y_end = list(map(int,input().split()))
    planet_num = int(input())
    planet_list = []

    for j in range(planet_num):
        x_target, y_target, rad_target = list(map(int,input().split()))
        if inclusion(x_end, y_end, x_target, y_target, rad_target) & ~inclusion(x_start, y_start, x_target, y_target, rad_target):
            planet_list.append([x_target,y_target,rad_target])
        if ~inclusion(x_end, y_end, x_target, y_target, rad_target) & inclusion(x_start, y_start, x_target, y_target, rad_target):
            planet_list.append([x_target,y_target,rad_target])
    
    print(len(planet_list))
