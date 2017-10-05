#!/usr/bin/env python3

#pylint: disable = dangerous-default-value

# -------------------
# FunctionDefaults.py
# -------------------

print("FunctionDefaults.py")

def f (x, y, z = 4) :
    return [x, y, z]

assert f(2, 3)    == [2, 3, 4]
assert f(2, 3, 5) == [2, 3, 5]

# def g (x, y = 3, z) : # SyntaxError: non-default argument follows default argument
#     return [x, y, z]

def g (x = 2, y = 3, z = 4) :
    return [x, y, z]

assert g()         == [2, 3, 4]
assert g(5)        == [5, 3, 4]
assert g(5, 6)     == [5, 6, 4]
assert g(5, 6, 7)  == [5, 6, 7]
assert g(5, z = 7) == [5, 3, 7]

print("Done.")
