import random
#in this season the user choses the last number of the range
top_of_range = input("Type a number, it will be the limit of the range: ")

top_of_range = int(top_of_range)
#this condition verifies if the last number is bigger than zero
if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
 print('Please type a number next time.')
quit()
#the line bellow serves for
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")