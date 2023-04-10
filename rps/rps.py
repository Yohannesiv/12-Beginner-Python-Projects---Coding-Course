import random
def play():
    user = input("choose 'r' for rock, 'p' for paper and 's' for scissors\n").lower()
    computer = random.choice(["r", "p", "s"])
    
    if user == computer:
        print("It's a tie")
    elif is_win(user, computer):
        print("Yayy, you won")
    else:
        print("sorry You have lost, try again")

def is_win(player, opp):
    #r > s, s > p , p > r
    if (player == "r" and opp == "s") or (player == "s" and opp == "p") or (player == "p" and opp == "r"):
        return True
play()