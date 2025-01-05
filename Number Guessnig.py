import random

EASY = 10
HARD = 5

def level(inp):
    if inp == "hard":
        return HARD
    else:
        return EASY

def compare(num1,num2):
    if num1 > num2:
        return "too high"
    elif num1 < num2:
        return "too low"

def game():
    print(logo)
    answer = random.randint(1,100)
    print(f"Psst, {answer}")
    choose = input("easy or hard? : ").lower()
    loop = level(choose)

    while loop > 0:
        print(f"u have {loop} attempts left")
        guess = int(input("Make a guess : "))
        print(compare(guess,answer))
        loop -= 1
        if guess == answer:
            loop = -1
            print(f"you got it, the ans is {answer}")
        elif guess != answer:
            print("guess again")

        if loop == 0:
            print("you lose")

game()
