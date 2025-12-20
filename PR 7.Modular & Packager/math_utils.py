import math 
import math

def basic_math():
    a = float(input("Enter number A: "))
    b = float(input("Enter number B: "))
    print("Add:", a + b)
    print("Subtract:", a - b)
    print("Multiply:", a * b)
    print("Divide:", a / b)

def trig_functions():
    x = float(input("Enter angle in degrees: "))
    rad = math.radians(x)
    print("Sin:", math.sin(rad))
    print("Cos:", math.cos(rad))
    print("Tan:", math.tan(rad))

def factorial():
    n = int(input("Enter number: "))
    print("Factorial:", math.factorial(n))

def compound_interest():
    p = float(input("Principal: "))
    r = float(input("Rate: "))
    t = float(input("Time: "))
    amount = p * (1 + r/100)**t
    print("Compound Interest:", amount)

def show_math_menu():
    print("\n1. Basic Arithmetic")
    print("2. Trigonometric Functions")
    print("3. Factorial")
    print("4. Compound Interest")

    ch = input("Enter choice: ")

    if ch == "1":
        basic_math()
    elif ch == "2":
        trig_functions()
    elif ch == "3":
        factorial()
    elif ch == "4":
        compound_interest()
        