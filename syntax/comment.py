#!/usr/bin/python
# -*- encoding: utf-8 -*-

## 行注释 标识符 '#'
# this is the first line comment
spam = 1 # and this is the second comment
        # ... and now a third!
text = "# this is not a comment becasue it's inside quotes."

print "spam =", spam
print "text=", text

## 块注释 标识符 '"""'
## 块注释一般用在代码文件的开头, 对整个文件的功能进行描述
print '""" ... """ is a example of block comment'
"""
This file is used to test how to use comment in Python
Python 默认使用 ASCII 字符集, 当代码文件里面含有Non-ASCII字符时候
需要显示的注明使用的字符集, 比如UTF-8字符集
"""
