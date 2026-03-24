import random

print("🎮 Welcome to Number Guessing Game!")

# Computer random number choose karega
number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break