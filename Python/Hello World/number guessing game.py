
num = 9
lower_range = 1
upper_range = 20
bit_range = 4
guessed = int(input("Type a number between 1 and 20: "))


while guessed != num:

    if (num - bit_range) < guessed < num:
        print("\nNumber is bit higher.")
    elif num < guessed < (num + bit_range):
        print("\nNumber is bit lower.")
    elif lower_range <= guessed <= (num - bit_range):
        print("\nNumber is higher.")
    elif upper_range >= guessed >= (num + bit_range):
        print("\nNumber is lower.")
    elif guessed < lower_range or guessed > upper_range:
        print("\nNumber is out of range.")
    guessed = int(input("\nType a number between 1 and 20: "))


if guessed == num:
    print("\nGREAT!! You guessed it right!")
