import re

with open("hashes.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    username, hashvalue = line.strip().split(":")

    is_hex = bool(re.fullmatch(r"[0-9a-fA-F]+", hashvalue))
    length = len(hashvalue)

    print("Username:", username)
    print("Hash:", hashvalue)
    print("Length:", length)
    print("Hexadecimal:", is_hex)

    if length == 40 and is_hex:
        print("Likely hash type: SHA-1")
    else:
        print("Hash type: unknown")

    print("-" * 50)
