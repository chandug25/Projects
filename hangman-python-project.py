import random
print("Welcome to the Hangman GAME!")
random_words=["marvel","harrypotter","thor","groot","captainamerica"]
word=random.choice(random_words)
n=len(word)
list=["_"]*n
print(list)
i=0
n=len(list)
count=n
chances=0
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
k=6
while True:
    if count==0:
        print("Game Over , You Won ! ")
        print(f"You took {chances} to finish this game")
        break
    g=input("letter:").lower()
    chances=chances+1
    if g in word:
        for i in range(len(word)):
            if(g.lower()==word[i].lower()):
                list[i]=g.lower()
                count=count-1
        print(list)
    else:
        if k==0:
            print("Hangman Died, You Lost the GAME!")
        print("try again")
        print(stages[k])
        k=k-1
        
    n=n-1
          
            
            
        
