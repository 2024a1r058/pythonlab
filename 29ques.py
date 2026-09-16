#WAP to take a word and count the number of vowels a,e,i,o,u
word=input("Enter word")
count=0
for ch in word:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        count=count+1
print("count",count)
# WAP to take a word and count the number of vowels a,e,i,o,u
# word = input("Enter word: ")
# count = 0
# for ch in word:
#     if ch in "aeiou":
#         count += 1
# if count > 0:
#     print("Number of vowels:", count)
# else:
#     print("No vowels found")
