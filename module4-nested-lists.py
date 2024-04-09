#List of integers
numbers = [1, 2, 3, 4]

#List of strings
countries = ["UK", "US", "Germany"]

#List of integers and Strings
countries = [1, "UK", 2, "US"]

#Nested list
cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]

#Returns a sublist
print(cells[0])

#Returns an element within the sublist
print(cells[0][0])
print(cells[0][1])
print(cells[1][2])

cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]

#Iterate through the sublists
for x in cells:
    print("Element:", x)

#iterate through all elements within each sublist
for x in cells:
    for y in x:
        print("Element:", y)

#Same iteration with different variable names
table = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for row in table:
    for cell in row:
        print("Element:", cell)

#Print in table format
table = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for row in table:
    for cell in row:
        print(cell, "", end="")
    print()
    

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [i for i in range(1, 6) for j in range(4)]
print(table)