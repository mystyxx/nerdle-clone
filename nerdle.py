from random import *

def newEquation():
    a = randint(1, 20)
    b = randint(1, 10)

    operators = ['*', '+', '-']
    operator = randint(0,3)


    if operator == 0:
        return (str(a) + operators[operator] + str(b) + '=' + str(a*b))
    if operator == 1:
        return (str(a) + operators[operator] + str(b) + '=' + str(a+b))
    if operator == 2:
        return (str(a) + operators[operator] + str(b) + '=' + str(a-b))
    

eq = str(newEquation())
# print(eq, len(eq))
guesses = 0

while guesses<5:

    feedback = []

    for i in range(len(eq)):
        print("_", end="")
        feedback.append(0)
    print("")
    
    answer = input()
    for i in range(len(answer)):
        if answer[i] in eq:
            feedback[i]=1
        if answer[i] == eq[i]:
           feedback[i]=2

    if 0 not in feedback and 1 not in feedback:
        print("You win !")
        exit()    
    else:
        guesses+=1
        pass

    if guesses >=5:
        print("perdu !")
        exit()

    for i in feedback:
        print(i, end='')
    print("", end="\n\n")

