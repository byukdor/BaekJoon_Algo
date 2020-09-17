import sys
student_list = list(range(1,31))

for i in range(28):
    student_list.remove(int(sys.stdin.readline()))

for i in range(2):
    print(student_list[i])