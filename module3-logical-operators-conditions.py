# available logical operators
# 
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equals
# != not equals

password = input("Do you know the secret password?")
if password != '--secret':
    print("Not correct")
else:
    print("Correct password")


if True: #Always runs
    print("Condition met")

if False: # Never runs
    print("Condition not met")
    
if 2 == 2:
    print('true')
    
if 1 == 2:
    print('false')

if 2 == 2.0:
    print("true")
