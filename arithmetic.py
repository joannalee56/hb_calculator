"""Functions for common math operations."""

#Functions for reduce
def add2(num1, num2):
    return num1 + num2

def subtract2(num1, num2):
    """Return the value of num1 minus num2."""
    return num1 - num2

def multiply2(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    return num1 * num2

def divide2(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    return num1 / num2

def square2(num1):
    """Return the square of num1."""
    return num1 * num1

def cube2(num1):
    """Return the cube of num1."""
    return num1 * num1 * num1

def power2(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1 ** num2

def mod2(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1 % num2



# We wrote out the functions for additional integers
def add(nums):
    """Return the sum of integers."""
    result = 0
    for num in nums: 
        result += int(num)
    return result


def subtract(nums):
    """Return the subtractration of integers."""
    result = int(nums[0])
    for num in nums[1:]: 
        result -= int(num)
    return result


def multiply(nums):
    """Multiply the two inputs together."""
    result = 1
    for num in nums: 
        result *= int(num)
    return result


def divide(nums):
    """Divide the first input by the second, returning a floating point."""
    result = int(nums[0])
    for num in nums[1:]: 
        result /= int(num)
    return result


def square(nums):
    """Return the square of the input."""
    if len(nums) == 1:
        result = int(nums[0]) * int(nums[0])
    else:
        result = "Please enter valid numbers for calculation."
    return result


def cube(nums):
    """Return the cube of the input."""
    if len(nums) == 1:
        result = int(nums[0]) * int(nums[0]) * int(nums[0])
    else:
        result = "Please enter valid numbers for calculation."
    return result

def power(nums):
    """Raise num1 to the power of num and return the value."""
    if len(nums) == 1:
        result = "Please enter valid numbers for the power function."
    elif len(nums) == 2:
        result = int(nums[0]) ** int(nums[1])
    elif len(nums) > 2:
        result = int(nums[0])
        for i in range(1, len(nums) - 1): 
            result = result ** (int(nums[i]) ** int(nums[i+1]))
    return result


def mod(nums):
    """Return the remainder of num / num2."""
    if len(nums) == 1:
        result = "Please enter valid numbers for the mod function."
    else:
        result = int(nums[0])
        for num in nums[1:]: 
            result %= int(num)
    return result

