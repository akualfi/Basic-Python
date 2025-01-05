from art import logo
print(logo)
dictionary = {}

def highest():
    num = 0
    winner = ""
    for bidder in dictionary:
        if num < dictionary[bidder]:
            num = dictionary[bidder]
            winner = bidder
    return f"The winner is {winner} with bid {num}"

def inp_dict(user,money,dictio):
    dictio[user] = money

def main():
    start = True
    while start:
        name = input("What's ur name? : ")
        bid = int(input("You bid? : $"))
        option = input("Any other? y or n :")
        inp_dict(name,bid,dictionary)
        print("\n"*100)
        if option == "n":
            start = False
            print(highest())

main()