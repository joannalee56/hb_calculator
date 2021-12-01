"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

calculator_on = True
result = None

while(calculator_on):
    token = input("Enter calculation: ").split(' ')[0:3]
    x = int(token[1])
    
    if len(token) == 2:
        y = None
    elif len(token) == 3:
        y = int(token[2])
    elif len(token) > 3: 
        result = "Please enter valid calculation"

    if token[0] == "q":
        calculator_on = False
    else:
        if token[0] == "+":
            result = add(x, y)
        elif token[0] == "-":
            result = subtract(x,y)
        elif token[0] == "*":
            result = multiply(x,y) 
        elif token[0] == "/":
            result = divide(x,y)
        elif token[0] == "sq":
            result = square(x)
        elif token[0] == "cube":
            result = cube(x)
        elif token[0] == "**":
            result = power(x, y)
        elif token[0] == "%":
            result = mod(x, y)
            
    print(result)