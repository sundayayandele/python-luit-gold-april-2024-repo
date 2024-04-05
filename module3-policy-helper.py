days = int(input("How many days ago have you purchased the item? "))
usage = input("Have you used the item at all [y/n]? ")
broken = input("Has the item broken down on its own [y/n]? ")

if (days <= 10 and usage == 'n') or (broken == 'y'):
    print("You can get a refund.")
else:
    print("You cannot get a refund.")
