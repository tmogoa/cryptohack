# Euclidean algorithm
# Author: Tony Mogoa

def gcd_iterative_1(a, b):
    while(a != b):
        if a > b:
            a = a - b;
        elif b > a:
            b = b - a;
    return a;

def gcd_iterative_2(c, d):
    while(c % d != 0):
        r = c % d
        c = d
        d = r
    return d

def gcd_recursive(c, d):
    if c % d == 0:
        return d
    else:
        return gcd_recursive(d, c % d)

def gcd_extended(a, b):
    if a == 0:
        return b ,0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y



print ("GCD:")
print(gcd_extended(26513, 32321))