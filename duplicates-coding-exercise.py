def unique(input_list=[]):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(unique([1, 1, 4, 5, 1]))
print(unique(['Mark', 'Mark', 'John', 'Anne']))