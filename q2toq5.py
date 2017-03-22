#!/usr/bin/env python2.7

import re


def convert(a=''):
    int_pattern = r"^[0-9]+$"
    float_pattern = r"^[0-9]*.[0-9]+$"

    if re.match(int_pattern, a):
        return int(a)
    elif re.match(float_pattern, a):
        return float(a)
    else:
        return a


def find_minimum(num1, num2, num3):
    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3

    return minimum


def apply_operation(left_operand, right_operand, operator):
    operator_dict = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': (lambda x, y: x * y),
                     '/': (lambda x, y: float(x) / float(y))}
    return operator_dict[operator](left_operand, right_operand)


def reformat_output(animal, name, age):
    output = ('{name} the {animal} is {age} years old'.format(animal=animal, name=name, age=age))
    print output

if __name__ == "__main__":
    print type(convert('1'))
    print type(convert('1.0'))
    print type(convert('asdf'))
    print ""
    print ""
    reformat_output('dog', 'Fido', 10)
    print ""
    print ""
    print find_minimum(4, 3, 5)
    print ""
    print ""
    print apply_operation(2, 3, '+')
    print apply_operation(2, 3, '-')
    print apply_operation(2, 3, '*')
    print apply_operation(2.0, 3.0, '/')
