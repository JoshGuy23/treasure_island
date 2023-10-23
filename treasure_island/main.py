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
path = input().lower()

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
            print("Which door do you go through?")
            choice_a2 = input().lower()
            if choice_a2 == "r":
                print("Your character finds themselves in a room of fire. Game Over.")
            elif choice_a2 == "b":
                print("Your character finds themselves in a room full of beasts.")
                print("Your character triumphs over the beasts and finds two secret passages.")
                print("Do you go down the left corridor (L) or the right corridor (R)?")
                choice_a3 = input().lower()
                if choice_a3 == "l":
                    print("Your character finds themselves in front of a mysterious door.")
                    print("Your character enters. Their mind cannot comprehend what lies beyond. Game Over.")
                elif choice_a3 == "r":
                    print("Your character finds a treasure chest! After confirming that it's not a mimic, they open the chest for their reward!")
                    print("Your character found some treasure! Congratulations! You may either stop playing, or play again to find the other treasures.")
                else:
                    print("While your character is twiddling their thumbs from an incorrect input, they are jumped by some still-conscious beasts. Game Over.")
            elif choice_a2 == "y":
                print("Your character found some treasure! Congratulations! You may either stop playing, or play again to find the other treasures.")
            else:
                print("Since you entered an incorrect value, your character simply dies of contrivance. Game Over.")
elif path == "r":
    if character != "b":
        print("In your character's way is a puzzle. However, your character failed the puzzle, and fell into a trap door. Game Over")
    else:
        print("Your character solves the puzzle flawlessly, and moves on.")
        print("Your character finds a library whose front door is locked by a puzzle.")
        print("Should your character (A) Knock on the door, or (B) Solve the puzzle.")
        choice_b1 = input().lower()
        if choice_b1 == "a":
            print("The door opens - and out comes the Grim Reaper, annoyed that his nap was interrupted. Game Over.")
        elif choice_b1 == "b":
            print("Your character solves the puzzle and enters the library - quietly, of course.")
            print("Your character finds themselves in a large, voluminous library.")
            print("To your right is the Grim Reaper, napping on a rocking chair. Not that you needed extra incentive to be quiet in a library.")
            print("You come across a hallway, and find three doors.")
            print("There is a red door (R), a blue door (B), and a yellow door (Y).")
            print("Which door do you go through?")
            choice_b2 = input().lower()
            if choice_b2 == "r":
                print("Out from the red door comes a blast of fire.")
                print("You are burnt to a crisp, and the library is set aflame. The Grim Reaper is not happy. Game Over.")
            elif choice_b2 == "b":
                print("In the room lies a pedestal holding a mysterious, weathered tome.")
                print("On the floor is a flask filled with mercury.")
                print("Upon reading the tome, you come across two spells that seem useful. But you only have enough energy to case one.")
                print("(A) A spell to summon a 'Philosopher's Stone'")
                print("or")
                print("(B) A spell called 'Wish'")
                choice_b3 = input().lower()
                if choice_b3 == "a":
                    print("You summon a philospher's stone, which you use to change the mercury into gold.")
                    print("Your character found some treasure! Congratulations! You may either stop playing, or play again to find the other treasures.")
                elif choice_b3 == "b":
                    print("You cast Wish, and wish for a treasure chest. One appears - several feet above your head, and crashes down. Game Over.")
                else:
                    print("While messing around, you accidentally summon a dark monster. A dark, hungry monster. Game Over.")
            elif choice_b2 == "y":
                print("Your character found some treasure! Congratulations! You may either stop playing, or play again to find the other treasures.")
            else:
                print("Your character, bored from the incorrect input, leans against a bookshelf.")
                print("Your character accidentally topples the bookshelf and many others.")
                print("The Grim Reaper woke up, and he is not happy. Game Over.")
        else:
            print("Your character gets distracted by an incorrect input and fails the puzzle, opening the trap door beneath them. Game Over.")
else:
    print("Your character sits down, indecisive, and falls into an eternal sleep. Game Over. (You must enter 'L' or 'R')")
