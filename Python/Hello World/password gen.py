from random import *

# for numbers
num_print_no = 0
num_password = []

while num_print_no != 4:
    num = str(randint(0, 9))
    num_password.extend(num)
    num_print_no += 1

numbers = num_password[0] + num_password[1] + num_password[2] + num_password[3]

cap_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"
cap_letter_pass = choice(cap_letter)

# for letters
letter_ = "thelazydogjumpsoverthequickbrownfox"

letter_print_no = 0
letter_password = [""]

while letter_print_no != 5:
    letter = choice(letter_)
    letter_password.extend(letter)
    letter_print_no += 1

letters = cap_letter_pass + letter_password[0] + letter_password[1] +\
          letter_password[2] + letter_password[3] + letter_password[4]


# for letters
spl_character = "/.,?><;:'\"\[]{}"

spl_chr_print_no = 0
spl_chr_password = [""]

while spl_chr_print_no != 2:
    spl_charac = choice(spl_character)
    spl_chr_password.extend(spl_charac)
    spl_chr_print_no += 1

spl_chr = spl_chr_password[2] + spl_chr_password[1]

print(letters + numbers + spl_chr)
