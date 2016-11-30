#!/usr/bin/python
# -*- coding: utf-8  -*-

the_world_is_flat = 1
if the_world_is_flat:
	print "Be careful not to fail off!"


# x = int(raw_input("Please enter an integer: ") # Why not works TODO
x = int('12')
if x < 0:
	x = 0;
	print 'Negative changed to zero'
elif x == 0:
	print 'Zero'
elif x == 1:
	print 'Single'
else:
	print 'More'


