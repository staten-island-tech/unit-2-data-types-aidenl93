""" def login(password):
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("whats password")
login(x) """

"""def grade(score):
    if score >= 92:
        print("A")
    elif score >= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F")
x = int(input("Whats score"))
grade(x)"""

def gamble(age,id):
    if age >= 21:
        if id: 
            print("gamble")
        else:
            print("show id")
    else:
        print("too young")