#!/usr/bin/env python3
def islower(x):
    ascii_value = ord(x)

    if ascii_value >= 97 and ascii_value <= 122:  # ASCII values for 'a' to 'z'
            return True
    else:
        return False   


print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))