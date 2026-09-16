#WAP to take a string and separate characters present at5 even index position and odd index position

word = input("Enter a word: ")

even_chars = ""
odd_chars = ""

for i in range(len(word)):
    if i % 2 == 0:
        even_chars += word[i]
    else:
        odd_chars += word[i]

print("Characters at even indices:", even_chars)
print("Characters at odd indices:", odd_chars)
