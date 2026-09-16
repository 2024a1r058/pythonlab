#WAP to input a number ans check whether it is prime or not. A number is prime if it has no divisor other than 1 and itself.
n = int(input("Enter a number: "))
if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")