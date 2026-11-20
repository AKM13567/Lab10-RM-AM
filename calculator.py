# https://github.com/AKM13567/Lab10-RM-AM.git
# Partner 1 - Aarya Maskara
# Partner 2 - Ruteshkhanna Manikhandhan

import math

def square_root(a):
    if a < 0:
        raise ValueError("The square root function does not accept negative numbers.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return square_root(a**2 + b**2)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a) 
def exponent(a, b):
    return a ** b