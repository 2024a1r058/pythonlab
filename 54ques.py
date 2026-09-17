#WAP to input numbers in a list and create two separate lists for even and odd numbers
numbers=list(map(int,input("enter numbers:").split()))
even_list=[]
odd_list=[]
for n in numbers:
    if n%2==0:
        even_list.append(n)
    else:
        odd_list.append(n)
print("Even elements:",even_list)
print("odd elements:",odd_list)