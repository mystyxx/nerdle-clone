from random import *

def newEquation():
    a = randint(1, 20)
    b = randint(1, 10)

    operator = randint(0,3)
    operators = ['*', '+', '-']


    if operator == 0:
        return (str(a) + operators[operator] + str(b) + '=' + str(a*b))
    if operator == 1:
        return (str(a) + operators[operator] + str(b) + '=' + str(a+b))
    if operator == 2:
        return (str(a) + operators[operator] + str(b) + '=' + str(a-b))
    

eq = str(newEquation())
# print(eq, len(eq))
guesses = 0
allowedchar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=', '+', '-', '*']

class notAnEquation(Exception):
    "Raised when the guess is not an equation"
    pass
class lettersInGuess(Exception):
    "Raised when there are something other than numbers and operators in the guess"
    pass
class guessDoesNotCompute(Exception):
    "Raised when the guess is mathematically incorrect"
    pass

def main(guesses):

    feedback = []
    for i in range(len(eq)):
        print("_", end="")
        feedback.append(0)
    print("")

    answer = input()

    if len(eq) != len(answer):
        raise IndexError
    elif '=' not in answer:
        raise notAnEquation
    splittedAnswer = answer.split('=')
    if eval(splittedAnswer[0]) != int(splittedAnswer[1]):
        raise guessDoesNotCompute 
    
    for i in range(len(answer)):
        if answer[i] not in allowedchar:
            raise lettersInGuess
        if answer[i] in eq:
            feedback[i]=1
        if answer[i] == eq[i]:
            feedback[i]=2
                

    if 0 not in feedback and 1 not in feedback:
        print("You win !")
        exit()
    else:
        for i in feedback:
            print(i, end='')
        print("", end="\n\n")
        return guesses+1



while guesses<5:
    try:
        guesses = main(guesses)
    except IndexError:
        print("Guess length not valid !")
        pass
    except notAnEquation:
        print("Guess must be an equation !")
        pass
    except lettersInGuess:
        print("Guess must contain only ints and operators, except / and % !")
        pass
    except guessDoesNotCompute:
        print("Guess doesn't compute !")
        pass
print("You lost !")