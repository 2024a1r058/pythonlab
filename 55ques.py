#WAP to rotate a list one position to the right
numbers = list(map(int, input("Enter numbers: ").split()))

last = numbers.pop()
numbers.insert(0, last)

print("Rotated list:", numbers)