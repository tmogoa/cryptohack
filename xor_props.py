from pwn import *
# XOR'ing the XOR result with a XOR operand gives us the other operand

# Convert to bytes first

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# get KEY2 by XOR'ing KEY1 and the result
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# get KEY3 by XOR'ing KEY2 from above and the result
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
# XOR KEY1, KEY2 and KEY3 and use the result to XOR with the result to get the flag

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2 = xor(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"), KEY1);
KEY3 = xor(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"), KEY2);

xord_key_123 = xor(KEY1, KEY2, KEY3)

flag = xor(xord_key_123, bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))

print(flag)