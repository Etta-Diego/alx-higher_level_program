#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    maxi = my_list[0]
    if my_list is None:
        return None
    for num in range(len(my_list)):
        if my_list[num] > maxi:
            temp = my_list[num]
            my_list[num] = maxi
            maxi = temp
    return maxi
