# Rock, Paper Scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

from random import randint

op_list = [rock, paper, scissors]

user_selection = op_list[
    int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
]
comp_selection = op_list[randint(0, len(op_list) - 1)]

if (user_selection == comp_selection):
    print(f"{user_selection}\nYour selection\n{comp_selection}\nComputer selection")
    print("Draw!")
elif (
    user_selection == rock
    and comp_selection == scissors
    or user_selection == paper
    and comp_selection == rock
    or user_selection == scissors
    and comp_selection == paper
):
    print(f"{user_selection}\nYour selection\n{comp_selection}\nComputer selection")
    print("You win!")
else:
    print(f"{user_selection}\nYour selection\n{comp_selection}\nComputer selection")
    print("You lose!")
