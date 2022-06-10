import random

while True:

    # user=input(f'Enter your choice{"R":"ROCK","P":"PAPER","S":"SCISSORS"}Use R for rock and P for paper and S for scissors: ')
    inputs={"R":"ROCK","P":"PAPER","S":"SCISSORS"}
    user = input("Enter your choice (rock, paper, scissors) Use R for rock and P for paper and S for scissors: ").upper()
    # inputs={"R":"rock","P":"paper","S":"scissors"}
    # inputs[user]=user

# if type.upper()=='K':
#     print('Your weight in pounds is ... ',str(int(weight)*2.204623))

# output=""
# for eachnumber in phonenumber:
#     output+=numberdictionary.get(eachnumber,"!")+' '
# print(output)



    possible_inputs = ["ROCK", "PAPER", "SCISSORS"]
    CPU = random.choice(possible_inputs)

    print(f'\nPlayer ({inputs.get(user)}): CPU  ({CPU})\n')

    if inputs.get(user)   == CPU:
        print(f"Both players selected the same move: '{inputs.get(user)}', It's a tie!")
    elif inputs.get(user)   == "ROCK":
        if CPU == "SCISSORS":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif inputs.get(user)   == "PAPER":
        if CPU == "ROCK":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif inputs.get(user)   == "SCISSORS":
        if CPU == "PAPER":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    restart = input("Play again? (y/n): ")
    if restart.lower() != "y":
        break

