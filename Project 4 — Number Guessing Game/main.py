import random

number = random.randint(1, 100)

print("🎯 Number Guessing Game")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too Low! Try again.")
    elif guess > number:
        print("Too High! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number.")
        break