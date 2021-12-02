"""CLI application for a prefix-notation calculator."""

from arithmetic import (add2, subtract2, multiply2, divide2, square2, cube2,
                        power2, mod2, add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce
 
calculator_on = True
result = None

while(calculator_on):
    try:
        token = input("Enter calculation: ").strip().split(' ')
        nums = [float(num) for num in token[1:]]
        print(nums)
        x = int(token[1])
    
        if len(token) == 2:
            y = None
        elif len(token) == 3:
            y = int(token[2])
        elif len(token) > 3: 
            result = "Please enter valid calculation"

        if token[0] == "q":
            calculator_on = False
        # Using Reduce function (for chain of inputs)
        else:
            if token[0] == "+":
                result = reduce(add2, nums)
            elif token[0] == "-":
                result = reduce(subtract2, nums)
            elif token[0] == "*":
                result = reduce(multiply2, nums) 
            elif token[0] == "/":
                result = reduce(divide2, nums)
            elif token[0] == "sq":
                result = square2(nums[0])
            elif token[0] == "cube":
                result = cube2(nums[0])
            elif token[0] == "**":
                result = reduce(power2, nums)
            elif token[0] == "%":
                result = reduce(mod2, nums)
            else:
                result = "Woops! Please enter valid operator."

        # If not using reduce function
        # else:
        #     if token[0] == "+":
        #         result = add(nums)
        #     elif token[0] == "-":
        #         result = subtract(nums)
        #     elif token[0] == "*":
        #         result = multiply(nums) 
        #     elif token[0] == "/":
        #         result = divide(nums)
        #     elif token[0] == "sq":
        #         result = square(nums)
        #     elif token[0] == "cube":
        #         result = cube(nums)
        #     elif token[0] == "**":
        #         result = power(nums)
        #     elif token[0] == "%":
        #         result = mod(nums)
        #     else:
        #         result = "Woops! Please enter valid operator."
                
        print(result)

    except ValueError:
        print("Oops! That was not a valid number.")