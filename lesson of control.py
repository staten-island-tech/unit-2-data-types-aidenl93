def login(password):
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("whats password")
login(x)