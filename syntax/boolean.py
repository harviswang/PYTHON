#!/usr/bin/python
# -*- encoding: utf-8 -*-

print True
print False
print

def binary_test(x, y):
    print x, '&', y, '=', x & y
    print x, '|', y, '=', x | y
    print '!', x, '=', not(x)      # Python not support ! operator, using not() instead
#    print x, '&&', y, '=', x && y # Python not support && operator,
#    print x, '||', y, '=', x || y # Python not support || operator,
    print 

binary_test(True, False)
