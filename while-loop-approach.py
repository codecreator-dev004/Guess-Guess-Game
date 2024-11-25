# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random # import the file random 
n = random.randint(1,100) # create a variable name n and use the property of random using randint from 1 to 100
user_guess = 1  # create a variable given value to 1
a = -1 # take value of a is -1 
while(a!= n):  # the condition of while is never change because of n is start with postive number and a is -1
   a = int(input("Guess The Number : ")) 
   if(a > n):
      print("Lower Number Please")
      user_guess += 1
   elif(a < n):
      print("Higher Number Please")
      user_guess += 1

print(f"You have guesses the number {n} correctly in {user_guess} attempts.")
    
