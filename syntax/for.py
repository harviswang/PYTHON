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

