"""
rsa_test.py
Purpose: uses an example of the RSA algorithm
Author: Michael Probst
"""

import sys
import Crypto.PublicKey.RSA as RSA


# create the private key
secret_code = "Password"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")

file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

# read private key
secret_code = "Password"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)

print(key.publickey().export_key().decode("utf-8"))
