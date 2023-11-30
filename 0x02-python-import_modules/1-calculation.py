#!/usr/bin/python3
from calculation_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    plus = add(a, b)
    diff = sub(a, b)
    multiply = mul(a, b)
    division = div(a, b)
    print("{} + {} = {}".format(a, b, plus))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, multiply))
    print("{} / {} = {}".format(a, b, division))
