import random
number = random.randint(0,10)


for i in range(3):
    guess = int(input("Enter a number betwen 0 and 10: "))
    if guess < number:
        print("Too Low")
    elif guess > number :
        print("Too High")
    else:
        print("Correct")
        break

else:
    print("Sorry, you did not guess the number. It was", number )