import random

print("ROCK PAPER SCISSORS!")
print("Who reaches 5 points wins!")

item = ["rock", "paper", "scissors"]

player_pts = 0
comp_pts = 0
cap = 5


while player_pts != cap and comp_pts != cap:
    comp_choice = random.choice(item)
    player_choice = input("\nRock/Paper/Scissor: ").lower()
    if player_choice == "rock":
        if comp_choice == "rock":
            player_pts += 0
            comp_pts += 0
        if comp_choice == "scissors":
            player_pts += 1
            comp_pts += 0
        if comp_choice == "paper":
            player_pts += 0
            comp_pts += 1

    elif player_choice == "paper":
        if comp_choice == "rock":
            player_pts += 1
            comp_pts += 0
        if comp_choice == "scissors":
            player_pts += 0
            comp_pts += 1
        if comp_choice == "paper":
            player_pts += 0
            comp_pts += 0

    elif player_choice == "scissors":
        if comp_choice == "rock":
            player_pts += 0
            comp_pts += 1
        if comp_choice == "scissors":
            player_pts += 0
            comp_pts += 0
        if comp_choice == "paper":
            player_pts += 1
            comp_pts += 0
    else:
        print("VOID")
    print("                   I choose: " + str(comp_choice).upper())
    print("       Your points: " + str(player_pts) + "         My points: " + str(comp_pts))


if player_pts > comp_pts:
    print("YOU WIN!")
else:
    print("YOU LOSE!")
