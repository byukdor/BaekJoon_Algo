a_num = "4"
b_list = "1 -1 3 -5"


b_list = list(map(int,b_list.split()))
sub_list = []

if a_num > 2:
    for i in range(1,int(a_num)):
        sub_list.append(b_list[i]-b_list[i-1])
        
    if (sub_list[0] == sub_list[1]) and not (sub_list[1] / sub_list[0]) == (sub_list[2]/ sub_list[1]):
        a = 0
        b = sub_list[0]
        print(int(b_list[int(a_num)-1]*a+b))
    elif (sub_list[1] / sub_list[0]) == (sub_list[2]/ sub_list[1]) and not (sub_list[0] == sub_list[1]):
        a = sub_list[2] / sub_list[1]
        b = b_list[1] - b_list[0] * a
        print(int(b_list[int(a_num)-1]*a+b))
    elif (sub_list[0] == sub_list[1]) and (sub_list[1] / sub_list[0]) == (sub_list[2]/ sub_list[1]):
        print("A")
    else:
        print("B")
else:
    print("A")

#b = list(map(int,input().split()))
