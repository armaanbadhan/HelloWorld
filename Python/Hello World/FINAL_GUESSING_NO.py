from random import *

print("WELCOME TO NUMBER GUESSING GAME!!")


def game():
    difficult = input("\nEasy/Medium/Hard: ").lower()

    upper_range = int()
    bit_range = int()
    tries = 0

    if difficult == "easy":
        upper_range = 10
        bit_range = 2
        tries += 4
    elif difficult == "medium":
        upper_range = 20
        bit_range = 4
        tries += 7
    elif difficult == "hard":
        upper_range = 40
        bit_range = 8
        tries += 10
    else:
        print("Enter a valid difficulty")

    print("You have " + str(tries) + " tries.")

    lower_range = 1
    num = randint(1, upper_range)

    guessed = int(input("\nType a number between 1 and " + str(upper_range) + ": "))
    no_guessed = 1

    while guessed != num and no_guessed != tries:
        if (tries - 1) == no_guessed:
            print('"LAST TRY"')
        if (num - bit_range) < guessed < num:
            print("\nNumber is bit higher.")
        elif num < guessed < (num + bit_range):
            print("Number is bit lower.")
        elif lower_range <= guessed <= (num - bit_range):
            print("Number is higher.")
        elif upper_range >= guessed >= (num + bit_range):
            print("Number is lower.")
        elif guessed < lower_range or guessed > upper_range:
            print("Number is out of range.")
        guessed = int(input("\nType a number between 1 and " + str(upper_range) + ": "))
        no_guessed += 1

    if guessed == num:
        print("GREAT!! You guessed it right! You took " + str(no_guessed) + " tries.")
    else:
        print("YOU LOSE! Correct answer was " + str(num) + ".")


game()

cont = int(input("\nPress 1 to continue, 0 to exit: "))

while True:
    if cont == 1:
        game()
        cont = int(input("\nPress 1 to continue, 0 to exit: "))
    else:
        print("Thanks for playing")
        exit()
