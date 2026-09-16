#WAP to repeatedly calculate the sum of digits of a number until the result become a single digit
a=int(input("enter a number"))
sum=0
while a>9 or sum>9:
    if a>9:
        digits=a%10
        sum=sum+digits
        a=a//10
    else:
        a=sum
        sum=0
print(a)

