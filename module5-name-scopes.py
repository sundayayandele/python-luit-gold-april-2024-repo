def show_truth():
    global mysterious_var #This lets the function know to use the global variable instead
    mysterious_var = "New Surprise!" #This is called shadowing. This is a local variable
    print(mysterious_var)


mysterious_var = "Surprise!" #The mysterious_var variable must be defined otherwise there will be an error. This is a global variable
print(mysterious_var)
show_truth()
print(mysterious_var)

def show_truth2():
    mysterious_var.append("New Surprise!") # this will change the global variable since it is not using =
    print(mysterious_var)

mysterious_var = ["Surprise"]
print(mysterious_var)
show_truth2()
print(mysterious_var)
