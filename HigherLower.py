logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from game_data_HiLo import data
import random

def name(num):
    return data[num]['name']
def desc(num):
    return data[num]['description']
def country(num):
    return data[num]['country']
def follower(num):
    return data[num]['follower_count']

def a(num):
    return f"{name(num)}, a {desc(num)}, from {country(num)}"
def b(num):
    return f"{name(num)}, a {desc(num)}, from {country(num)}"

def game():
    score = 0
    start = True
    index_a = random.randint(1, len(data))
    data.remove(data[index_a])
    index_b = random.randint(1,len(data))
    data.remove(data[index_b])

    while start:
        print(logo)
        if score > 0:
            print(score)
        start = True

        index_c = random.randint(1,len(data))

        print(f"Compare A: {a(index_a)}")
        print(vs)
        print(f"Against B: {b(index_b)}")
        choose = input("who has more followers? a or b : ").lower()

        if follower(index_a) > follower(index_b):
            if choose == "a":
                index_a = index_b
                index_b = index_c
                score += 1
                print("\n"*50)
            elif choose == "b":
                start = False
                print("\n" * 50)
                print(score)
        elif follower(index_a) < follower(index_b):
            if choose == "b":
                index_b = index_c
                score += 1
                print("\n"*50)
            elif choose == "a":
                start = False
                print("\n" * 50)
                print(score)

game()
