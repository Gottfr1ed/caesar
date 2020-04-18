#!/usr/bin/env python3
import sys


def encrypt(plaintext, key):
    encrypted = ""

    for c in plaintext:
        if c.isalpha():
            if c.islower():
                c = chr((ord(c) - 97 + key) % 26 + 97)
            else:
                c = chr((ord(c) - 65 + key) % 26 + 65)
        encrypted += c

    return encrypted


def decrypt(ciphertext, key):
    decrypted = ""

    for c in ciphertext:
        if c.isalpha():
            if c.islower():
                c = chr((ord(c) - 97 + 26 - key) % 26 + 97)
            else:
                c = chr((ord(c) - 65 + 26 - key) % 26 + 65)
        decrypted += c

    return decrypted


def print_usage():
    print("usage: ./caesar -e text -k 15 (-d for decryption)")


if len(sys.argv) != 5:
    print_usage()
    sys.exit(1)

if "-e" not in sys.argv and "-d" not in sys.argv or "-k" not in sys.argv:
    print_usage()
    sys.exit(1)

key = sys.argv[sys.argv.index("-k")+1]

try:
    key = int(key)
except ValueError:
    print("the key must be an integer")
    sys.exit(1)

key = (key % 26 + 26) % 26  # the key will always be 0-25

if "-e" in sys.argv:
    print(encrypt(sys.argv[sys.argv.index("-e")+1], key))
else:
    print(decrypt(sys.argv[sys.argv.index("-d")+1], key))
