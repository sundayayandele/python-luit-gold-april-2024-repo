sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    eng_word = input("Enter a word in English or EXIT: ")
    if eng_word == "EXIT":
        print("Bye!")
        break
    elif eng_word in sample_dict:
        print("Translation:", sample_dict[eng_word])
    else:
        print("No match!")
