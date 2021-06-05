
print("           You have three tries \n".upper())
print("'Enter in lower case'")

secret_word = "physics"
guessed_word = ""
guess_count: int = 0
out_of_guesses = False

while secret_word != guessed_word and not out_of_guesses:
    if guess_count < 3:
        if guess_count == 1 and guessed_word == "maths":
            print("Nice try but it's not MATHS... 2 tries left!")
        if guess_count == 1 and not guessed_word == "maths":
            print("2 tries left!")
        if guess_count == 2:
            print("Last try!")
        guessed_word = input("Guess a subject which involves numbers: ")
        guess_count += 1
    else:
        out_of_guesses = True


TRY = ""
if guess_count == 1:
    TRY = "try"
else:
    TRY = "tries"


if out_of_guesses:
    print("\n       YOU LOSE! Correct word was \"physics\".")
else:
    print("\n    Woah!! You Win! You guessed it in " + str(guess_count) + " " + TRY + "!")
