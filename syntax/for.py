#!/usr/bin/python
# -*- encoding: utf-8 -*-

words = ['cat', 'window', 'defenestrate']
for w in words:
	print w, len(w)

for w in words[:]: # Loop over a slice copy of the entire list
	if len(w) > 6:
		words.insert(0, w)

print words
print

## range(x) -> [0, x)
## range(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10): # [0, 10), step is 1
	print i,
print

for i in range(10, 30): # [10, 30), step is 1
	print i,
print

for i in range(10, 30, 5): # 10 means start, 30 means end, 5 means step
	print i,
print

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i], len(a[i])
print

## for with break/else
## 这里的 else: 锁进和上面的 for 对齐, else clause belongs to the for loop, 
## not the if statement
## 内层 for 循环 执行了 break 则 else 不会执行
## 内层 for 循环 没有执行 break, 则 else 会执行

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break;
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'
print

## loop with continue
for x in range(0, 10):
    if x % 2 == 0:
        print x, "is an even number"
        continue # since x + 1 % 2 must not be zero, so can skip it to speed up
