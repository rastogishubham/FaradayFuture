#!/usr/bin/env python2.7

import re


# Function to convert string to either int, float or string depending on input
def convert(a=''):
    int_pattern = r"^[0-9]+$"  # Regex to check if input is an integer
    float_pattern = r"^[0-9]*.[0-9]+$"  # Regex to check if input is a floating point number

    # If it is an integer, or a floating point number convert to that type and return, otherwise return string
    if re.match(int_pattern, a):
        return int(a)
    elif re.match(float_pattern, a):
        return float(a)
    else:
        return a


# Function to find minimum of three numbers without using inbuilt min function
def find_minimum(num1, num2, num3):
    minimum = num1  # Set minimum to be first number

    # if number 2 is less than minimum, set minimum to be number 2
    if num2 < minimum:
        minimum = num2
    # if number 3 is less than minimum, set minimum to be number 3
    if num3 < minimum:
        minimum = num3

    return minimum


# Function to apply operation on operands passed to the function
def apply_operation(left_operand, right_operand, operator):
    """ Creation of dictionary with lambda functions based on
        operator input as key and the operation being
        performed on the operands as the value
    """
    operator_dict = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': (lambda x, y: x * y),
                     '/': (lambda x, y: float(x) / float(y))}
    return operator_dict[operator](left_operand, right_operand)


# Function to reformat output based on input strings and print the output
def reformat_output(animal, name, age):
    output = ('{name} the {animal} is {age} years old'.format(animal=animal, name=name, age=age))
    print output


if __name__ == "__main__":
    print "Testing Question 2:"
    print ''
    print ''
    print "Test case 1: type(convert('1'))"
    print type(convert('1'))
    print "Test case 2: type(convert('1.0'))"
    print type(convert('1.0'))
    print "Test case 3: type(convert('asdf'))"
    print type(convert('asdf'))
    print ''
    print ''
    print "Testing Question 3:"
    print "Test case: abc = {'dog', 'Fido', 10}"
    abc = ['dog', 'Fido', 10]
    reformat_output(abc[0], abc[1], abc[2])
    print ''
    print ''
    print "Testing Question 4:"
    print "Test case: find minimum of 4, 3, 5"
    print "Minimum is:"
    print find_minimum(4, 3, 5)
    print ""
    print ""
    print "Testing Question 5:"
    print "Test case 1: apply_operation(2, 3, '+')"
    print apply_operation(2, 3, '+')
    print "Test case 2: apply_operation(2, 3, '-')"
    print apply_operation(2, 3, '-')
    print "Test case 3: apply_operation(2, 3, '*')"
    print apply_operation(2, 3, '*')
    print "Test case 4: apply_operation(2, 3, '/')"
    print apply_operation(2.0, 3.0, '/')
