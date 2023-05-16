# AES & RSA Test

## Requirements
The implementations of the encryption algorithms are implemented in python. The examples created require python 3.x

The algorithms come from the [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html) library. Install this library with the command: `python3 -m pip install pycryptodome`

## Q1
The first question uses an implementation of AES. The example program is set up so that you must enter a string that guesses the plaintext of the encrypted key. This is meant to demonstrate a successful and unsuccessful key pairing. The correct phrase to pass as an argument is: **0123456789ABCDEF**

use the example program with the following command: `python3 aes_test.py '<your_string>'`

## Q2
The second question uses an implementation of RSA to create a private key. It is used in an example to generate a key, and that key is then read and if the correct passphrase is given, the example will run successfully. The password is hard-coded into the example, so to run this example simply enter the command: `python3 rsa_test.py`
