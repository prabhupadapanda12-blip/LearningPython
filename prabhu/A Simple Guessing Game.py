secret_number = 7
guess = 0

print("I'm thinking of a number between 1 and 10. Can you guess it?")


while guess != secret_number:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You win!")