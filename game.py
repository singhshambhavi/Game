import random

def get_guess():
    return input("Whats your guess")

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clue(code,user_guess):
    if user_guess==code:
        return "Code Craked"
    clue=[]#enmpty list and add as we go through user guess

    for ind,num in enumerate(user_guess): #ind is for index
        if num==code[ind]:
            clue.append("match")
        elif num in code:
            clue.append("close")
    if clue==[]:
        return("Nope")
    else:
        return clue

print("Welcome !")
secrete_code = generate_code()

clue_report = []

while clue_report!="Code Cracked":
    guess=get_guess()
    clue_report=generate_code(guess,secrete_code)
    for clue im clue_report:
        print(clue)