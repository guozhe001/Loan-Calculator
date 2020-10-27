# Make sure your output matches the assignment *exactly*
spend_on_computer_hours = int(input())

if spend_on_computer_hours < 2:
    print("That seems reasonable")
elif spend_on_computer_hours >= 4:
    print("Don't forget to take breaks!")
else:
    print("Do you have time for anything else?")
