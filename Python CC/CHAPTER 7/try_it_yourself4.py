prompt = "\nTell me your pizza topping:"
prompt += "\nEnter 'quit' to end the program. "
while True:
    toopings = input(prompt)
    if toopings == 'quit':
        break
    else:
        print(f"Adding the {toopings} to your pizza")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
while True:
    userage = int(input("Enter you age or enter '0'to quit"))
    if userage == 0:
        break 
    if userage < 3:
        print("The ticket is free")
    elif userage >= 3 and userage <= 12:
        print("The ticket price is $10")
    else:
        print("The ticket price is $15")