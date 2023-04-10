import random
x = int(input("your upper limit is: ")) 
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high #it also colld be low because low  == high
        feedback = input(f"Is {guess} too high (H), too low (L) or corrct(C)").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print (f"yayy, the computer guessd your number {guess} correctly")
computer_guess(x)