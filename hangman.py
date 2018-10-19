#!/usr/bin/python
import random 
worddb = open("worddb.txt",mode="r")
words = []
for i in worddb.readlines():
    if i != "\n":
        words.append(i.replace("\n",""))
hangman =[ """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___""" , 
    """
      _______
     |/      |
     |      (_)
     |       |/
     |       |
     |      / \\
     |
    _|___  _  """,
 """
      _______
     |/      |
     |      (_)
     |       |/
     |       |
     |      /   
     |
    _|___  _  _ """,

 """
      _______
     |/      |
     |      (_)
     |       |/
     |       |
     |          
     |
    _|___  _ _ _ """,
"""
      _______
     |/      |
     |      (_)
     |       | 
     |       |
     |          
     |
    _|___  _ ___ """,

 """
 ( x__x ) DEAD
    ||
    ||
"""]


def game():
    skor = 0
    wrongcount = 0
    print("*"*10+"Welcome to a new game"+"*"*10)
    print(hangman[0])
    keyword = random.choice(words)
    key = keyword
    table = "_"*len(keyword)
    this_round = "static"
    while this_round == "static":
        print(table)
        #print(keyword)
        guess = input("Which letter you want to reveal?\n>>")
        if keyword.count(guess) >= 1:
            skor += keyword.count(guess)
            temp_table = [i for i in table]
            while keyword.count(guess) > 0:
                temp_table[keyword.index(guess)] = guess
                keyword = keyword.replace(guess,"*",1)
                #print(keyword)
            table = "".join(temp_table)
        else:
            wrongcount +=1 
            print(hangman[wrongcount])
        if table == key:
            print("Keyword was",key)    
            print("====YAY You win !====")
            endinput = input("Enter 'q' to quit\nPress enter to start a new game\n")
            if endinput.lower() == "q":
                this_round = "changed"
            else:
                print("Starting a new game...")
                game()
        if wrongcount == 5:
            print("Keyword was",key)    
            endinput = input("Enter 'q' to quit\nPress enter to start a new game\n")
            if endinput.lower() == "q":
                this_round = "changed"
            else:
                print("Starting a new game...")
                game()


game()    
