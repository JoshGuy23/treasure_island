print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print('''Are you:
A. Athletic
or
B. Intelligent?''')
character = input().lower()

if character == "a":
    print("Your character is Athletic.")
elif character == "b":
    print("Your character is Intelligent.")
else:
    print("Your character is Normal.")

print("The path splits in two. Do you go left (L) or right (R)?")
path = input().lower

if path == "l":
    if character != "a":
        print("Your character fell into a hole. Game Over.")
    else:
        print("Your character gracefully leaps over the hole.")
        print("Your character comes across a lake. If you want to swim, enter 1. If you want to wait for a boat, enter any other number.")
        choice_a1 = int(input())
        if choice_a1 != 1:
            print("The boat arrives, only for your character to come face-to-face with the Grim Reaper. Game Over.")
        else:
            print("Your character swims to the other side of the lake.")
            print("Your character finds themselves in front of three doors.")
            print("There is a red door (R), a blue door (B), and a yellow door (Y).")
elif path == "r":
    if character != "b":
        print("In your way is a puzzle. However, your character failed the puzzle, and fell into a trap door. Game Over")
else:
    print("Your character sits down, indecisive, and falls into an eternal sleep. Game Over. (You must enter 'L' or 'R')")