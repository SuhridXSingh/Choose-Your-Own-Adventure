name = input("Type your Name: ")
print("Welcome to this adventure",name,"!!")

answer = input("You're lost in a dense forest. You only have two choices, set up a base and wait for help or move towards where you think you came from.").lower()
if answer == "set up a base and wait for help":
    answer = input("You have found a perfect open area to set up a base and a dry den on the other hand. open or den? ").lower()
    if answer == "open":
        print("It was extremely chilly weather which led to severe frostbites resulting in your death. Game Over!")
    elif answer =="den":
        answer = input ("Conratulations! You made it through the night. But you notice a small bite mark on your arm. ignore or use the only band aid you have? (Ignore/treat)").lower()
        if answer == "ignore":
            print("Congratulations! You saved a band aid but unfortunately you're dead. Game Over!")
        elif answer == "treat":
            print("You waited the whole day and as the sun was about to set, you heard voices of people talking, when you followed the voice you saw that there was a group of people partying there. You were saved! YOU WIN!!")
        else:
            print("Game Over!!!")
    else:
        print("Invalid! Game Over!")
elif answer == "move towards where you think you came from":
    answer=input("You have walked for 5 hours and there's still no way back to be found. You wasted most of your resources. head back or keep moving?").lower()
else:
    print("Not a valid answer, You're Dead. Game Over!")
