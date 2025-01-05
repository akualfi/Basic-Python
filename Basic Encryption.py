alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def choose(user,num):
    if user == "encode":
        num *= 1
        return num
    elif user == "decode":
        num *= -1
        return num

def system():
    print(logo)

    yes = True
    while yes:
        chosen = input("encode or decode:\n").lower()
        message = input("Your message:\n").lower()
        shift = int(input("The shift number:\n"))

        words = ""
        for letter in message:
            if letter in alphabet:
                shifted = alphabet.index(letter) + choose(chosen, shift)
                shifted_new = shifted % len(alphabet) # IMPORTANT
                words += alphabet[shifted_new]
            else:
                words += letter

        print(f"This is your {chosen} result: {words}")

        option = input("Want again? y or n: ")
        if option == "n":
            yes = False

system()



