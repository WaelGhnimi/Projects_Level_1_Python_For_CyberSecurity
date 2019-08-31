#DiceGame
import random
import time

roll_again = "YES"
yes_list = ["YES","Y"]
while roll_again in yes_list:
    print("\nRolling the dice...")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The value are :")
    print("Dice 1 =", dice1, "\nDice 2 =", dice2)

    if dice1 == dice2:
        print("=================== # WINNER ! :You rooled a double! # =====================")

    else:
        print("Keep trying!")

    roll_again = input("\nRoll the dice again? (Y/N)").upper()

