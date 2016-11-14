#!/usr/bin/python

import sys

index = 0
for arg in sys.argv:
	print 'argv[', index, '] = ', arg
	index = index + 1
