#Results in both variables having the same value
first = input("Enter the first number: ")
second = input ("Enter the second number: ")
print("Before swapping:", first, second)
first = second
second = first
print("After swapping:", first, second)

#Correclty swaps the two numbers using a temp variable
first = input("Enter the first number: ")
second = input ("Enter the second number: ")
print("Before swapping:", first, second)
temp = first
first = second
second = temp
print("After swapping:", first, second)

#More efficient way of swapping the variables
first = input("Enter the first number: ")
second = input ("Enter the second number: ")
print("Before swapping:", first, second)
first, second = second, first
print("After swapping:", first, second)

#Swapping with list elements
top_cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]
top_cities.sort()
print(top_cities)

#Changes the list
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

#does no change the original list
top_cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(sorted(top_cities))
print(top_cities)