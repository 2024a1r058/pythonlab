#WAP to input a decimal number and convert it into binary without using built-in function
decimal=int(input("Enter a decimal number:"))
if decimal==0:
   binary=="0"
else:
    binary=""
    temp=decimal

    while temp>0:
        remainder=temp%2
        binary