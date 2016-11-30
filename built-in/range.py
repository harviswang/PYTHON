#!/usr/bin/python
# -*- encoding: utf-8 -*-

## one parameter
## generate a sequence of numbers, [0, second_parameter)
## with one increasing step 
print range(10)
print

## two paramteters
## generate a sequence of numbers, [first_parameter, second_parameter)
## with one increasing step 
print range(2, 10)
print

## three parameters
## generate a sequence of numbers, [0, second_parameter) with the increasing step 
## from the third_parameter
print range(2, 10, 3)
print

## work with len() to iterate over the indices of a sequence
## range() here used to generate the indices of a sequence
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for i in range(len(week)):
    print i, week[i]
