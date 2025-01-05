import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user = int(input("0 for rock, 1 for paper, 2 for scissors"))
computer = random.randint(0,2)

def choose(num):
    return game_images[num]

def game():
    print(choose(user))
    print("Comp choose" + choose(computer))
    if user == computer - 1 or user == computer - 2:
        print("You lose")
    elif user == computer + 1 or user == computer +2:
        print("You win")
    elif user == computer:
        print("Draw")

game()



