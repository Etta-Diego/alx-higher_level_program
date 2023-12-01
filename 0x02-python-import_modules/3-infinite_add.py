#!/usr/bin/python3
import sys
length = len(sys.argv
args_sum = 0
for arg in sys.argv[1:]:
    args_sum += int(arg)
print("{:d}".format(args_sum))
