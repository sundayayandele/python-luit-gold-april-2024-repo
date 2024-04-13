#if True:
#print("hooray!") Example of syntax error

#value = int(input("Enter an integer: "))
#print("The inverse of", value, "is", 1/value) #Gives an error if the type is wrong

try:
    value = int(input("Enter an integer: "))
    print("The inverse of", value, "is", 1/value)
except ValueError:
    print("You did not provide a number, so I will not calculate the inverse")
except ZeroDivisionError:
    print("You provided 0 and division by 0 is not possible, sorry")
except:
    print("Something strange happened here, sorry")