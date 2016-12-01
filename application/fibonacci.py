#!/usr/bin/python
# -*- encoding: utf-8 -*-

## fibonacci
## 0, 1, 1, 2, 3, 5, 8
## a0 = 0, a2 = 1
## an = an-1 + an-2 , n > 2

# Multiple assignment
a, b = 0, 1
while b < 1000:
	print b,
	a, b = b, a+b

## true: non-zero integer values
##       anything with a non-zero length
## flase: zero
##        empty sequences

## stand comparison oprators:
## <, >, ==, <=, >=, !=

## Indentation is Python's way of grouping statements

## print, a space is inserted between items
## a traling comma avoids the newline after the output
## ther interrepter inserts a newline before it prints the 
## next prompt if the last line was not completed. 
