correctNumber = 17
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please Guess Number : "))
    if userGuess > correctNumber:
        print("Too large")
    elif userGuess < correctNumber:
        print("Too Small")
    elif userGuess == correctNumber:
        print("correcting Number")

