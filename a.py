
def skins3(money, cost, available):
    while money > cost or available == False or money > cost and available == False:
        print("no money")
    print(f"current balance: {money}. \n current cost: {cost} go buy")
