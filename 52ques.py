#WAP to input numbers in a list and findthe second largest number
numbers=list(map(int,input("Enter numbers").split()))
maximum=max(numbers)
numbers.remove(maximum)
second_maximum=max(numbers)
print(second_maximum)