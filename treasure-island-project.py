
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You find yourself on a deserted beach. In the distance, you spot an island. What do you want to do? Type "swim" to swim to the island or "explore" to search the beach. \n').lower()

if choice1 == "swim":
    choice2 = input('You bravely swim to the island and reach its shores safely. On the island, you discover three paths. One leads into a dense jungle, another to a mysterious cave, and the third to a hill with a lone palm tree. Which path will you choose? Type "jungle," "cave," or "hill." \n').lower()
    
    if choice2 == "jungle":
        print("As you venture deeper into the jungle, you encounter wild animals and get lost. Game Over.")
    elif choice2 == "cave":
        print("You enter the dark cave, and it leads to a dead end. Game Over.")
    elif choice2 == "hill":
        choice3 = input("You climb the hill and find a hidden treasure chest! You open it and discover unimaginable wealth. You Win!")
    else:
        print("You're indecisive and remain on the beach. Game Over.")
else:
    print("While exploring the beach, you stumble upon a hidden treasure chest buried in the sand. You've found the treasure! You Win!")
print("GAME OVER!")