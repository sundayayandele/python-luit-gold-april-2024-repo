#Tuples are immutable just like Strings
empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3,
print(three_el_tuple)

user_data = ("John", "American", 1964)
user_data = ("Katya", "Russian", 1980)
#error cases
user_data.append("teacher")
del user_data(0)
print(user_data(0)) # This works
user_data(0) = "Mark" #This causes an error

