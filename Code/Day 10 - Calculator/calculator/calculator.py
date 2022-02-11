from art import logo
import os

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}

def calculator():
    print(logo)
    
    num1 = float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)        
    shouldContinue = True
    
    while shouldContinue == True:
        operationSymbol = input("Pick an Operation: ")
        num2 = float(input("What is the next number: "))
        calculationFunction = operations[operationSymbol]
        answer = calculationFunction(num1, num2)
        
        print(f"{num1} {operationSymbol} {num2} = {answer}")
        
        if input(f"type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            shouldContinue = False
            os.system("clear")
            calculator()
calculator()

