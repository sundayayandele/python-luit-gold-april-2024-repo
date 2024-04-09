import random

number = random.randint(0, 10)

if number < 6:
    print("small number")
elif number > 6:
    print("big number")
else:
    print("number is 6")
    
if number < 4:
    print("a really small number")
print(number)
