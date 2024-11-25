import random

n = random.randint(1, 100)
user_guess_value = 0
max_attempts = 10  # You can set the maximum number of attempts

for attempt in range(max_attempts):
    a = int(input("Enter your guess: "))
    user_guess_value += 1
    
    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print(f"Congratulations! You've guessed the number {n} in {user_guess_value} attempts.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {n}.")