name_original = "Jon Snow"
name_new = name_original

name_original = "Daernerys Targaryen"

print(name_original, name_new)

#Has the same reference
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print("New:", list_new, "\nOriginal", list_original)

#Creates a new list
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print("New:", list_new, "\nOriginal", list_original)

#Copies a portion of the list
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print("New:", list_new, "\nOriginal", list_original)
