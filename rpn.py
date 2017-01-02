__author__ = 'andrewpitts'
import sys

run = True

def calculate(input):
    numberStack = []
    input = input.split(' ')
    for i in input:
        if i == ' ':
            continue
        elif i == '+':
            numberStack.insert(0, numberStack.pop(0) + numberStack.pop(0))
        elif i == '-':
            numberStack.insert(0, numberStack.pop(1) - numberStack.pop(0))
        elif i == 'x' or i == '*':
            numberStack.insert(0, numberStack.pop(0) * numberStack.pop(0))
        elif i == '/':
            numberStack.insert(0, numberStack.pop(1) / numberStack.pop(0))
        elif i == '^':
            numberStack.insert(0, numberStack.pop(1) ** numberStack.pop(0))
        elif i.isdigit():
            numberStack.insert(0, int(i))
    return numberStack[0]


# print(calculate(input))

assert(calculate("5 2 3 ^ + 5 8 + ") == 13)
assert(calculate("3 2 * 11 -") == -5)
assert(calculate("2 1 12 3 / - + ") == -1)
assert(calculate("6 3 - 2 ^ 11 - ") == -2)
assert(calculate("6 3 2 ^ - 11 - ") == -14)
assert(calculate("162 2 1 + 4 ^ / ") == 2)
assert(calculate("2 4 - ") == -2)

print("****         RPN Calculator           ****")
print("****       Enter EXIT to quit         ****")
print("**** Separate all values with a space ****")
while run:
    userInput = input("Please input your RPN statement or EXIT to quit.")
    if userInput == "EXIT":
        sys.exit("Program ended.")
    testInput = userInput.split(' ')
    if len(testInput) < 3:
        print("Your RPN statement must be at least 3 characters long.")
    if testInput[-1].isdigit():
        print("Your RPN statement must end with an operand.")
    numCount = 0
    opCount = 0
    for i in testInput:
        if i.isdigit():
            numCount += 1
        if i == '+' or i == '-' or i == '*' or i == 'x' or i == '/' or i == '^':
            opCount += 1
    if numCount - 1 != opCount:
        print("Your RPN statement does not have enough operands.")
    else:
        print(calculate(userInput))