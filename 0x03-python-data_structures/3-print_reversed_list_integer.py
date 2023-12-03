def print_reversed_list_integer(my_list=[]):
    copy = my_list
    for ind in copy[::-1]:
        print("{:d}".format(ind))
