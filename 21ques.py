# #WAP to fill the given letter template with name and date
# name=input("enter name")
# date=input("enter date")
# letter=f"""
# Dear {name},
# You are selected!
# {date}
# """
# print(letter)
letter='''
Dear <Name>,
You are selected!
<Date>
'''
name=input("Enter name:")
date=input("Enter date:")

letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",date)

print(letter)