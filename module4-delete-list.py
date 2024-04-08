top_cities = ["New York City", "Los Angeles", "Singapore", "Chicago", "Houston", "Phoenix"]
del top_cities[2]
print(top_cities)
print(top_cities[2])
top_cities = ["New York City", "Los Angeles", "Singapore", "Chicago", "Houston", "Phoenix"]
del top_cities[3:]
print(top_cities)

top_cities = ["New York City", "Los Angeles", "Singapore", "Chicago", "Houston", "Phoenix"]
del top_cities[:]
print(top_cities)

#Cause an error as it completely deletes the list
del top_cities
print(top_cities)
