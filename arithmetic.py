"""Functions for common math operations."""


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

