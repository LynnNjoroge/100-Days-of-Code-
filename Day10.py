# Calculator Challenge
from calculator_art import logo
import os

def clear_console():
    os.system('clear')

print(logo)

def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """subtracts two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """multiplies two numbers"""
    return n1 * n2

def division(n1, n2):
    """divides two numbers"""
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division     
}

def calculator():
  num1 = float(input("What's the first number?: "))
  num2 = float(input("What's the next number?: "))
  #lets print out the operations for our user to see and choose
  for i in operations:
    print(i)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear_console()
      calculator()

calculator()