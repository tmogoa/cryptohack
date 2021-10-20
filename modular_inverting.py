# psuedo code
# find inverse given g element of F[p] and p
# formular g * inverse elem d ≡ 1 mod p
# in other words, (g * d) % p = 1
# (gd - 1) % p = 0
# d is any multiple of p, m, (m + 1) / g where (m + 1) % g = 0
# g is element of F[p] and p is prime
def modular_invert(g, p):
    counter = 1
    while True:
        multiple_of_p_add_one = (p * counter) + 1
        if multiple_of_p_add_one % g == 0 and multiple_of_p_add_one / g < p:
            print(multiple_of_p_add_one / g)
            break
        counter = counter + 1

modular_invert(3, 13) # 9

# p is prime
# g => elem of F[p]
# c => is a counter
def modular_invert_recursive(g, p, c):
    if (p * c + 1) % g == 0 and (p * c + 1) / g < p:
        return (p * c + 1) / g
    else:
        return modular_invert_recursive(g, p, c + 1)

print(modular_invert_recursive(8, 11, 1))
