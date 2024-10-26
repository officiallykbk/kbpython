from random import choice
from art import *
class hangman:
    words = ["tiger", "tree", "underground", "giraffe", "chair"]
    
    stages=["""
        ------
        | 
        | 
        |   
        |   
    """,
    """
        ------
        |    |
        |    O
        |   
        | 
    """,
    """
            ------
            |    |
            |    O
            |    |
            |   
    """,
    """
            ------
            |    |
            |    O
            |   /|\\
            |   
    """,
    """
            ------
            |    |
            |    O
            |   /|\\
            |   / \\
    """
    ]

    def __init__(self):
        self.word=choice(self.words)

       
        
        
        
start=hangman()

print("Solve the word puzzle ")
incomplete=[]
for i in start.word:
    incomplete.append("_ ")
    print('_ ',end="")       
chance=0
word=start.word
while (chance != 5):
    wordguess=str(input("\nGuess the word\n"))
    for i in wordguess:
        if i in start.word:
            print(f"{i} is correct")
            incomplete[start.word.index(i)]=i
            print(" ".join(incomplete))
        else:
           print(f"Sorry, {i} is not in the guess word.")
           print(start.stages[chance])
           print(" ".join(incomplete))
           chance+=1
if chance==5:
    print("You failed \n The word is\n")
    tprint(start.word)
    















