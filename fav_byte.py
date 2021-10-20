from pwn import *

bytes_ = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print(bytes_)

for i in range(256):

    print("KEY: " + str(i) + " => " + str(xor(bytes_, i)))