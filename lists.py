var = []

print(type(var))

var2 = [151, 251, 386, 493, 647, 721]
print(type(var), var2)

var3 = [151, 251, 386, 493, 647, 721, "009"]
print(type(var3), var3)

var3.append(445) #in place function. Changes happen in place
print(type(var3), var3)

var3 = var3 + [1008] # not in place
print(type(var3), var3)

print(dir(var3)) #Shows all available commands for a list

var4 = [0,1,2,3,4,5]

numbers = list(range(0, 10, 2))
print(numbers)
numbers = list(range(10))
print(numbers)

for number in numbers:
    print(type(number), number**2)

print(type(numbers), numbers[5])
numbers.reverse()
print(type(numbers), numbers)
print(type(numbers), numbers[5])
print(len(numbers))

list_of_lists = [[0,1,2], [3,4,5], [47,28,99]]

print(list_of_lists)

for element in list_of_lists:
    print(type(element), element)
    for number in element:
        print(type(number), number)
        
