var = {}
print(type(var))

var2 = {"juice": "cranberry", "movie": "The Lion King", "dessert": "cheesecake"}

print(type(var2), var2)

print(var2["juice"])

if "show" in var2:
    print(var2["show"])

var2["drink"] = "cola"
print(type(var2), var2)

del var2["drink"]
print(type(var2), var2)

print(dir(var2))

print(list(var2.keys()))
print(list(var2.values()))
print(list(var2.items()))

for k, v in var2.items():
    print(k, v)

var3 = {"a": {"d":"d"}, "b": {"e": "e"}, "c": {"f": "f"}}

for key, value in var3.items():
    print(key, value)
    for key2, value2 in value.items():
        print(key2, value2)