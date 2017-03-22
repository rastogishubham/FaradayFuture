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

if __name__ == "__main__":
    print type(convert('1'))
    print type(convert('1.0'))
    print type(convert('asdf'))