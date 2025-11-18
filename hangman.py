from random import *

words = ["apartment", "drumroll", "pingpong","bandana","sneakers"]
word_to_guess = choice(words)
print(word_to_guess)
len_wtg = len(word_to_guess)
placeholder = ""
guesses= 6

for position in range(len_wtg):
    placeholder += "_"

print("Word to guess:", placeholder)
game_on = True
correct_letters = []

while game_on:
    user_input = input("Guess a letter?")

    if user_input in correct_letters :
        print(f"You have already guessed the letter {user_input}")
    spaces = ""

    for letter in word_to_guess:
        if letter == user_input:
            spaces += letter
            correct_letters.append(user_input)
        elif letter in correct_letters:
            spaces+= letter
        else:
            spaces+= "_"

    print("Word to guess: " + spaces)

    if user_input not in word_to_guess:
        guesses -= 1
        print(f"You guessed {user_input},which is wrong. You lose a life")
        print(f"{guesses} LIVES LEFT")

        if guesses == 0:
            game_over = True
            print("You are dead")

            print(f"***********************YOU LOSE**********************\n The correct word is {word_to_guess}")

            replay = input("Do you want to play again?").lower()
            if replay == "yes":
                game_on = True
            elif replay== "no":
                game_on= False
            else:
                print("Invalid Input")

    if "_" not in spaces:
        game_on = False
        print("****************************YOU WIN****************************")

        replay = input("Do you want to play again?").lower()
        if replay == "yes":
            game_on = True
        elif replay == "no":
            game_on= False
        else:
            print("Invalid answer")



