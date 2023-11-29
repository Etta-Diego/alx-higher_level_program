#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            upper_c  = ord(c) - 32
        else:
           upper_c = ord(c)
        new_str += chr(upper_c)
#print("{}".formai(chr(new_str)), end="")
    print("{}".format(new_str))
