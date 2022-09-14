import unittest


def classify_triangle(a, b, c):
    result = ""
    if a == b and a == c and b == c:
        return 'Equilateral triangle'
    elif a == b or a == c or b == c:
        return 'Isosceles triangle'
    else:
        return 'Scalene triangle'
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return 'Right triangle'
    else:
        return 'Not a right triangle'
