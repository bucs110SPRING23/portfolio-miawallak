import random
number = random.randint(0,100)
number_guesses = 0

for i in range(101):
    guess = int(input("Enter a number betwen 0 and 100: "))
    number_guesses += 1
    if guess < number:
        print("Too Low")
    elif guess > number :
        print("Too High")
    else:
        print("Correct")
        break

print("Number of tries:", number_guesses)


