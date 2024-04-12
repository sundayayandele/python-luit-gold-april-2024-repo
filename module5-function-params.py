def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum+= number
    
    average = sum / len(input_numbers)
    
    print(average)

get_average([5.0, 3.5, 7.8, 9.9, 10.0])

#get_average() Causes an error
#get_average(5) Also causes an error as it is the wrong input type


def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print("Number of", letter, "is", counter)

print_letter_count("Welcome", "e")

print_letter_count("People say nothing is impossible, but I do nothing every day.", "a")

print_letter_count("e", "Welcome") #causes the wrong value. Order matters

#Both return the same value due to default values being set
print_letter_count(text="Welcome", letter="e")
print_letter_count(letter="e", text="Welcome")

