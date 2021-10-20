# p => modulo prime number
# b => modulo square
import math
# c => counter
def mod_sqrt(b, p, c):
    if abs(pow(c, 2) - b) % p == 0:
        return c
    if c == p - 1:
        return -1
    else:
        return mod_sqrt(b, p, c + 1)

sqrs = [14, 6, 11]
for sqr in sqrs:
    if(mod_sqrt(sqr, 29, 1) != -1):
        print(mod_sqrt(sqr, 29, 1))  # == 8

def mod_sqrt_loop(b, p):
    count = 1
    while True:
        if (pow(count, 2) - b) % p == 0:
            return count
        if(count == 1000):
            return -1;
        count = count + 1

#print(mod_sqrt_loop(6, 29)) # 8

# No answer for both
def mdl_sqrt(a, p):
    return pow(10, (math.log10(a) / (2 - p)))

print(mdl_sqrt(5, 29))