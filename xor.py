from pwn import *
str = "label"
xor_result = xor(str, 13)
print(xor_result)