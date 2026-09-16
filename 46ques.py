#ques 3 write a python program to print a right angled triangle using stars
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()