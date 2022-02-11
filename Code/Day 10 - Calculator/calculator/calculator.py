from art import logo
print(logo)

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

num1 = int(input("What is the first number: "))

for symbol in operations:
    print(symbol)
operationSymbol = input("Pick an Operation Symbol Above: ")
num2 = int(input("What is the second number: "))
calculationFunction = operations[operationSymbol]
answer = calculationFunction(num1, num2)

print(f"{num1} {operationSymbol} {num2} = {answer}")
