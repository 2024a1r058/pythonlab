principal=int(input())
rate=int(input())
time=int(input())
simple_interest=(principal*rate*time)//100
total_amount=principal+simple_interest
print(simple_interest)
print(total_amount)