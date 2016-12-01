#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
函数名字被解释器搜寻的先后顺序, 从先到后如下
1. local symbol table
2. local symbol tables of enclosing functions
3. global symbol table
4. table of built-in names
"""

## 定义函数 用内置方法 def
def fibonacci(n):
    """ calculate indexed fibonacci number """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for x in range(10):
    print fibonacci(x)

## fib is the same function object reference as fibonacci
fib = fibonacci
print fib(3)
print fibonacci(20)
print fib
print fibonacci

## 函数均有返回值
## 有 return x的函数, 返回值为 x
## 有 return 但是 没有参数的函数, 返回值为 None
## 没有 return 的函数, 返回值为 None
def no_return():
    pass
    return
print no_return()

## 计算不大于 n 的 fibonacci 列表
## 其中变量 b 是辅助变量
def fibonacci_list(n):
    a, b = 0, 1
    result = []             # Empty list
    while(a < n):
        result.append(a)    # result : a list object, append : a list method
        a, b = b, a+b
    return result

print fibonacci_list(100)
print

## function with default argument values
## the default values are evaluate at the point of function definition in the defining scope
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'yes', 'YES'):
            return True
        if ok in ('n', 'no', 'NO'):
            return False
        retries -= 1
        if retries < 0:
            raise IOError('refuseink user')
        print complaint

## invoke ask_ok
"""
print ask_ok('Do you really want to quit?')
print ask_ok('OK to overwrite the file?', 2)
print ask_ok('OK to overwrite the file?', 2, 'Come on, only yes/YES or no/NO!')
times=7
print ask_ok('Are you a man?', times)
"""

## the default value is evaluated only once
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f(1)
print f(2, f(1))
print f(3, f(2, f(1)))
print f(4, L=[5])
print f(L=[8], a=9) # keyword invoke
print

## Keyword Arguments
## 所有的函数参数名字都可以作为 keyword使用, 不管它后面有没有'='
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action
    print "if you put", voltage, "volts through it."
    print "--Lovely plumage, the", type
    print "-- It's", state, "!"

parrot(voltage=1000)  
parrot(voltage=1000000, action='VOOOOOM') 
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
                              # parrot() got multiple values for keyword argument 'voltage'
#parrot(actor='John Cleese')  # parrot() got an unexpected keyword argument 'actor'
print

## arguments : 
## keywords : keyword argument list
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40 # 打印40个 '-' 字符
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

cheeseshop("Limburge", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           chopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

## Arbitrary Argument Lists
## 使用 tuple 实现多参数的形式
def arbitrary_argument_function(*args):
    for index in range(len(args)):
        print "argument %d = %s" %(index, args[index])

arbitrary_argument_function(1, 2, 3, 4, 5)
print
