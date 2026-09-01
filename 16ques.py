#WAP to swap two integers without using third variable
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
a=a+b
b=a-b
a=a-b
print("After swapping a=",a)
print("After swapping b=",b)
