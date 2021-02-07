"""
aes_test.py
Purpose: tests the AES encryption algorithm
Author: Michael Probst
Solution based on: https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
"""

import argparse
import sys
import Crypto.Cipher.AES as AES


if len(sys.argv) == 1:
    print("Please enter a string as an argument to guess the key")
elif len(sys.argv) > 2:
    print("too many arguments. Only input the key string")
else:
    # create encoded message
    key = '0123456789ABCDEF'.encode()
    header = b'Dr Mani,'
    body = b'Hello!'

    cipher = AES.new(key, AES.MODE_CCM)
    cipher.update(header)
    message = cipher.nonce, header, cipher.encrypt(body), cipher.digest()
    
    # decrypt the message
    user_input = sys.argv[1]
    if len(user_input) != 16:
        print("WARNING: Key must be 16 char long.")
        user_input = '0000000000000000'
    nonce, header, ciphertext, mac = message 
    userkey = user_input.encode()
    d_cipher = AES.new(userkey, AES.MODE_CCM, nonce)
    d_cipher.update(header)
    plaintext = d_cipher.decrypt(ciphertext)
    try:
        d_cipher.verify(mac)
        print("The message is authentic:\n%s %s" % (header.decode("utf-8"), plaintext.decode("utf-8")))
    except:
        print("Key incorrect or message corrupted")
