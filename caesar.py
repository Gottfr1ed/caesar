#!/usr/bin/env python3
import sys

ALPHA_LEN = 26
LOWER = ord("a")
UPPER = ord("A")
USAGE = "usage: ./caesar -e text -k 15 (-d for decryption)"


def encrypt(plaintext, key):
    encrypted = ""
    for c in plaintext:
        if c.isalpha():
            if c.islower():
                c = chr((ord(c) - LOWER + key) % ALPHA_LEN + LOWER)
            else:
                c = chr((ord(c) - UPPER + key) % ALPHA_LEN + UPPER)
        encrypted += c
    return encrypted


def decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isalpha():
            if c.islower():
                c = chr((ord(c) - LOWER + ALPHA_LEN - key) % ALPHA_LEN + LOWER)
            else:
                c = chr((ord(c) - UPPER + ALPHA_LEN - key) % ALPHA_LEN + UPPER)
        decrypted += c
    return decrypted


if len(sys.argv) != 5:
    sys.exit(USAGE)
if "-e" not in sys.argv and "-d" not in sys.argv or "-k" not in sys.argv:
    sys.exit(USAGE)

# make sure we get an integer
key = sys.argv[sys.argv.index("-k") + 1]
try:
    key = int(key)
except ValueError:
    sys.exit("the key must be an integer")

# the key will always be in range 0-25
key %= ALPHA_LEN

if "-e" in sys.argv:
    print(encrypt(sys.argv[sys.argv.index("-e") + 1], key))
else:
    print(decrypt(sys.argv[sys.argv.index("-d") + 1], key))
