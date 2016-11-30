#!/usr/bin/python
# -*- encoding: utf-8 -*-

print 'this is a string enclosed in single quotes'  # 单引号包裹字符串
print "this is a string enclosed in double quotes"  # 双引号包裹字符串
print

## escape character
print '\"hello \t world\"' # backslash 是转义字符
print 'First line.\nSecond line.'  # \n means newline
print 'doesn\'t'  # use \' to escape the single quote...
print "doesn't"   # ...or use double quotes instead
print '"Isn\'t," she said.'
print

## raw string by adding an r before the first quot
print r'\"hello \t world\"'
print r'C:\some\name'  # note the r before the quote
print

## mutiple line string
## here backslash is line continuation character
print "China" \
      "America"
  
print """  # 多行字符串
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

print '''
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
'''
print

## 拼接
## * 倍数, + 拼接
print "# 3 times 'un', floowed by 'ium'"
print 3 * 'un' + 'ium'
print 'ba' + 2 * 'na'
print 'Py' 'thon' # Two or more string literals (i.e. the ones enclosed between quotes) 
                  # next to each other are automatically concatenated.
prefix = 'Li'
print prefix + 'sp' #  concatenate variables or a variable and a literal, use +

# here backlash is optional
text = ('Put several strings within parentheses ' \
        'to have them joined together.')
print text

## Python has no separate character type
## a character is simply a string os size one
## string index can be [0, string.length], [-string.length, -1]
word = 'Python Programming Language'
print word[-1] # -> e why? last character
print word[-2] # -> g second-last character
print word[-0]
print word[0]
print word[1]
print word[0:-1] # slicing, [0, -1)
print word[0:6] # slicing, [0, 6)
print word[:0] + word[0:] 
print word[:2]  # character from the beginning to position 2 (excluded)
print word[2:]  # characters from the second-last (included) to the end
print word[:2] + word[2:]
print word[:] # slice a new word, copy of ther original word
print

## Python string不能改变, immutable
# word[0] = 'J' #TypeError: 'str' object does not support item assignment
# 如果要改变一个string, 只能重新创建一个新string
word2 = 'J' + word[1:6]
print word2

## length of the Python string, using function len()
## str(int) -> string
print len(word2)
print 'len("how old are you")' + ' = ' + str(len("how old are you"))
print word2.format()  # ? TODO
print

## Unicode String
ustring = u'This is an Unicode String'
print ustring
# Unicode-Escape encoding, \u0020 means space in Unicode
print u'between A\u0020B is a space'
# Raw-Unicode-Escape encoding ? TODO
print ur'Hello\u0020World!'
print ur'Hello\\u0020World!'
print

## encode() -> unicode -> other encoding
## unicode() -> other encoding -> unicode
print unicode('A')
print str(u"abc")
print u"äöü".encode('utf-8')
print unicode(u"äöü".encode('utf-8'), 'utf-8')

## compare two string by operator ==, !=
## 
if "good" == "good":
	print "string can be compare by '==' operator"
if "good" != "bad":
	print "string can be compare by '!=' operator"
if "good" >= "bad":
	print "string can be compare by '>=' operator"
if "good" <= "luck":
	print "string can be compare by '<=' operator"
