#!/usb/bin/python
# -*- encoding: utf-8 -*-

## sequence can have different type
## can be indexed and sliced
squares = [1, 4, 9, 16, 25, '36']
print squares
print squares[0]  # indexing returns the item
print squares[-1]
print squares[2:] # slicing returns a new list
print squares[:]  # slice returns a new(shallow) copy of the list
print

## list concatenation
squares += [49, 64, 81, 100]
print squares
print

## list is a mutable type, it's content can be changed
cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3 # the cube of 4 is 64, not 65!
print 'cubes = ' + str(cubes)
print

## Assignment to slices is also possible, and this 
## can even hange the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print letters
# replace some values
letters[2:5] = ['C', 'D', 'E']
print letters
# Now remove them
letters[2:5] = [] # Empty list
print letters
# Clear the list by replacing all the elements with an empty list
letters[:] = []
print letters
print

## len() -> the lenth of list
print len([])
print len([1, 2, 3,])
print len([[1, 2, 3,], ['A', 'B', 'C']])
