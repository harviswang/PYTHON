#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys

class test:
    def __enter__(self):
        print("__enter__")
        return 1

    def __exit__(self, type, value, trace):
        print("__exit__")
        print "type ", type, " value ", value, " trace ", trace
        return True

def try_finally_test():
    t = test()
    try:
        t.__enter__()
        print("t = {0}".format(t))
    finally:
        t.__exit__(0, 0, 0)

try_finally_test()
print


# t is the value returned by __enter__()
with test() as t:
    print("t is not the result of test(), it is __enter__ returned")
    print("t is 1, yes, it is {0}".format(t))
    raise NameError("Hi there")

# file = open("/tmp/foo.txt", "wt") 
# try:
#     file.write("with xxx() as : test")
# finally:
#     file.close()
with open("/tmp/foo.txt", "wt") as file:
    file.write("with xxx() as : test")


