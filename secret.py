from pwn import *

hex_val = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
bytes_val = bytes.fromhex(hex_val)

print(bytes_val)
# xor first 7 bytes against first 7 bytes in the characters of the flag
print(xor(bytes_val, "crypto{")) # output is b'myXORke'

# we guess key to be b'myXORkey'
print(xor(bytes_val, "myXORkey"))
# we get the flag: b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
