first_direction = input("Would you like to go left or right?")
if first_direction == "left":
    print("you have entered a haunted house")
    print("you see a red door. you see a blue door. and you see a green door.")
    x = input("pick which door to go through;\nRED for the red door \nBLUE for the blue door \nGREEN for the green door")
    if x == "RED":
        print("you fall into a volcano and die")
    elif x == "BLUE":
        print("you fall into a pit of skeletons but still survive")
    elif x == "GREEN":
        print("you are safe")

if first_direction == "right":
    print("you have entered a dungeon")
    print("you hear sounds. you see a hallway. and there are stairs.")
    x = input("pick which to follow;\nSOUNDS for follow the sounds \nHALL for down the hallway \nSTAIRS for go up the stairs")
    if x == "SOUNDS":
        print("you get eaten by a monster and die")
    elif x == "HALL":
        print("the hallway keeps going")
    elif x == "STAIRS":
        print("you enter a room that has bats and you fight them off and survive")

second_direction = input("Would you like to go up or down?")
if second_direction == "up":
    print("you have entered a cloud")
    print("you see a waterfall. you see a garden.")
    second_direction = input("pick which room to go into;\nWATERFALL for the waterfall \nGARDEN for the garden")
    if second_direction == "WATERFALL":
        print("you drown in the waterfall and die")
    elif second_direction == "GARDEN":
        print("you find a secret passage that leads you out of the cloud and you survive")

if second_direction == "down":
    print("you have entered a bunker")
    print("you see a vault. you see a treasure chest.")
    second_direction = input("pick which to go to;\nVAULT for the vault \nCHEST for the treasure chest")
    if second_direction == "VAULT":
        print("the vault is filled with gold and you survive")
    elif second_direction == "CHEST":
        print("you find a vial that says you will have super powers but it is poison and you die")

third_direction = input("you have all the gold, would you like to keep it or trade it for something else?")
if third_direction == "keep":
    print("you gamble the gold and you become broke and you die")

if third_direction == "trade":
    print("you trade the gold for a magic sword and you survive")

fourth_direction = input("you have the magic sword, and you see a dragon. Would you like to fight it or hide from it?")
if fourth_direction == "fight":
    print("you fight the dragon and you win and you survive")
if fourth_direction == "hide":
    print("you hide from the dragon but it finds you and you die")


fifth_direction = input("good job you have survived so far this is the last level. Would you like to win or lose?")
if fifth_direction == "lose":
    print("you get shot up into outer space and you are stuck there for the rest of your life and you die")

if fifth_direction == "win":
    print("you become the king of the world you have won the game ")
    