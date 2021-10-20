# Find modulo
# a ≡ b (mod m)

def congruent_modulo(a, m):
    print(str(a) + " ≡ x mod " + str(m) + "; x = " + str(a % m))

def run_congruent_modulo():
    congruent_modulo(35 , 6)
    congruent_modulo(8146798528947, 17)


# Fermat's little theorem
def fermat_theorem_mod(base, exp, prime):
    if exp == prime:
        return base
    elif exp + 1 == prime and base % prime != 0:
        return 1
    else:
        return -1;
print(fermat_theorem_mod(273246787654, 65536, 65537))#  == 1

# Lets say we pick p = 17. Calculate 3^17 mod 17. Now do the same but with 5^17 mod 17.
#print("3^17 mod 17 = " + str(pow(3, 17) % 17));
#print("5^17 mod 17 = " + str(pow(5, 17) % 17));
print("3^17 mod 17 = " + str(fermat_theorem_mod(5, 17, 17)));
print("5^17 mod 17 = " + str(fermat_theorem_mod(3, 17, 17)));
# This is Fermat's little theorem a^p ≡ a (mod p)
# What would you expect to get for 7^16 mod 17? Try calculating that.
print("7^16 mod 17 = " + str(fermat_theorem_mod(7, 16, 17)));
# This is a special case of Fermat's little theorem a^(p - 1) ≡ 1 (mod p)
# This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.
# Now take the prime p = 65537. Calculate 273246787654 ^ 65536 mod 65537.
print("273246787654 ^ 65536 mod 65537 = " + str(fermat_theorem_mod(273246787654, 65536, 65537)));
# Did you need a calculator? No.

