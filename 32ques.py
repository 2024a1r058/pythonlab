#WAP to take a word and print it in reverse order using slicing. Also check whether it is same forward and backward
word=input("Enter word=")
reverse=word[::-1]
if word==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")