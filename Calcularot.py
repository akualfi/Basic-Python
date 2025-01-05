def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calc():
    f_num = float(input("First number: "))
    start = True
    while start:
        for i in operation:
            print(i)
        pick = input("Pick an operation: ")
        s_num = float(input("Next number: "))
        answer = operation[pick](f_num,s_num) # IMPORTANT
        print(f"{f_num} {pick} {s_num} = {answer}")
        choose = input(f"Type y to continue calc with {answer}, n to close : ")
        if choose == "n":
            start = False
            print("\n"*100)
            calc()
        else:
            f_num = answer

calc()


