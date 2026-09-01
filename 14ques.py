amount=int(input())
number_of_500_notes=amount//500
remaining=amount%500
number_of_100_notes=remaining//100
print(number_of_500_notes)
print(number_of_100_notes)