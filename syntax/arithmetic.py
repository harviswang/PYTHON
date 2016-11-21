## integer
print "2 + 2 =", 2 + 2
print "99 - -1 =", 99 - -1
print "5 * 6 =",  5 * 6
print "50 / 4 =", 50 / 4
print

## float
print "9.0 / 2 =", 9.0 / 2 # float / int -> float
print "8 / 5.0 =", 8 / 5.0 # int / float -> float
print "8 / 4 =", 8/4       # int / int -> int
print "17 // 3.0 =", 17 // 3.0 # explicit floor division discards the fractional part
print "9 % 4 =", 9 % 4
print

## power of
print "5 ** 2 =", 5 ** 2   # 25, 5 squared
print "2 ** 7 =", 2 ** 7   # 128, 2 to the power of 7
print

width = 20
height = 5 * 9
print "width * height =", width * height

print "3 * 3.75 / 1.5 =", 3 * 3.75 / 1.5   # operators with mixed type operands convert the integer operand to floating point
print "7.0 / 2 =", 7.0 / 2                 # 2 -> 2.0 before operation
print "7 / 2.0 =", 7 / 2.0                 # 7 -> 7.0 before operation

tax = 12.5 / 100
price = 100.50
print "round(price, 2) =", round(price, 2)

