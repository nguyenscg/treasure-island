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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
# Welcome to Treasure Island.
# Your mission is to find the treasure.
print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure. Good luck!")

firstpath = input('You arrived at a path, which way do you want to go? Type: "Left" or "Right"').lower()

if firstpath == "Left":
    secondpath = input("You see a dragon waiting at a post. The dragon offers you a ride. Type: 'Accept' or 'Decline'").lower()
    if secondpath == "Accept":
        lastpath = input("Which portal are you taking? Type: 'Red', 'Green', or 'Blue' ").lower()
        if lastpath == "Red":
            print("The portal teleported you to an area with trolls that attacked you.")
        elif lastpath == "Green":
            print("Yippie! You found the treasure! You may leave the island now.")
        elif lastpath == "Blue":
            print("The portal teleported you to the ocean. Game over!")
        else:
            print("You didn't pick a portal. Game over!")
    else:
        print("Game over! The dragon got annoyed and decided to eat you.")
else:
    print("You fell into a hole. Game over!")