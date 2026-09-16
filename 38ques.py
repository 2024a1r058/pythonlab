#WAP to check whether a number is perfect.A number is perfect if the sum of its proper division.
a=int(input("Enter a number:"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
if sum==a:
    print("Number is perfect")
else:
    print("Number is not perfect")