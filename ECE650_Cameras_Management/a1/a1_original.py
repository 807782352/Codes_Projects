#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author : Ziyi Xu
# Data : $October 11, 2021

import sys
from regex_check import regexFlag
from map_original import Map


# YOUR CODE GOES HERE
def main():
    # YOUR MAIN CODE GOES HERE

    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment
    map1 = Map()
    msg_print()
    while True:
        line = sys.stdin.readline()
        # print("read a line:", line)
        if line == "":
            break
        if regexFlag(line):
            map1.street_store(line)
        else:
            print("Format Wrong!")

    # print("Finished reading input")
    print("You have quited the system!")
    # return exit code 0 on successful termination
    sys.exit(0)


def msg_print():
    print("================================================")
    print("Welcome to Use the System!")
    print("Please Show Your Command Below:")
    print("* Use command add, mod, rm, gg to operate")
    print("* Use Ctrl-D to quit")
    print("================================================\n")


if __name__ == "__main__":
    main()
