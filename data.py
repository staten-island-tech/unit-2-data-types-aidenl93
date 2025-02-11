"""? # Strings are for representing characters, names, words, etc
name = "David"
# integer represents whole numbers
age: 14
#floats represent decimals
wallet = 5.45 
#boolean represents true/false, used in evaluations
graduated = False

def add(x,y):
    print(x+y)
#input asks the user a questions and stores response as value 
# bill = float(input("what was the bill?"))
# print(type(bill))
# add(40, bill)

#lists""" 
""" students = ["Joanna", "Deivid", "David", "Other David", "Ethan"]
#similar to saying for i in range(5): print(students[i])
print(students[4])
for student in students:
    print(student)
moneys = [1,2,3,4,5,6]
for money in moneys:
    print(money)
total = 0 """
""" x = "thingy"
y = x.split()
z = y[0]
print(y)
print(z)""" 
# make function for sentence
# count words for user
# state number of words
""" def sentence(input): # function for sentence, name of function is "sentence)"
    print(input) # print the input for sentence
sentence("Please make a sentence.") # print the input, input is in parentheses """

#DAY 2
# SPLIT SPLITS THE SENTENCE INTO INDIVIDUAL WORDS INTEAD OF RECOGNIZING THE ENITRE PHRASE AS A WHOLE
# LEN COUNTS THE LENGTH OF THE ENTIRE PHRASE

""" userin = input("Please make a sentence")
words = userin.split()
print(len(words))"""

""" weather = input("What's the weather like?").strip()
if weather == "Cold": 
    print("correct")
else: 
    print("incorrect") """


""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" yes = input("enter number")
if yes[-1] in "02468":
    print("even")
else:
    print("odd") """

""" def bill (tip):
    if tip >= 0:
        print("bad")
    if tip >= 15:
        print("okay")
    if tip >= 20:
        print("good")
    if tip >= 25:
        print("great")
money = int(float(input("Please tip a certain amount, From 0-25%")))
bill(money) """

"""def factors(x):
    list = []
    for i in range(1, x + 1):
        if x % i == 0:
            list.append(i)
    return list 

y = int(input("give number"))

print(f"factors: {factors(y)}")"""

def gcf(x,y):
    while y != 0: 
        x, y = y, x % y
    return x

bro = int(input("give num1"))
bro2 = int(input("give num2"))

bro3 = gcf(bro,bro2)
print(f"the gcf is {bro3}")
    
