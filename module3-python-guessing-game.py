correct_guess = 1994
while True:
    year_guess = int(input("When was Python 1.0 released? "))
    if year_guess == correct_guess:
        print("Correct!")
        break
    elif year_guess > correct_guess:
        print("It was earlier than that!")
    elif year_guess < correct_guess:
        print("It was later than that!")