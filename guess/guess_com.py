import random
x = int(input("the upper limt for the guess: "))
def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_num:
            print("sorry, guess again too low!")
        elif guess > random_num:
            print("sorry, guess again too high")
    print(f"yayy, congrats you have guessd the number {random_num}")
guess(x)