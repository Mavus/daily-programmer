#!/usr/bin/python
"""
Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!
[MAIN]: DONE
[EXTRA]: DONE
"""
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def caesar(symbol, shift = -3):
    c_alphabet = alphabet[shift:] + alphabet[:shift]
    if symbol in alphabet:
        return c_alphabet[alphabet.index(symbol)]
    else:
        return symbol

def encrypt(plaintext):
    return ''.join(map(caesar, plaintext))

def decrypt(ciphertext):
    return ''.join([caesar(c,3) for c in ciphertext])