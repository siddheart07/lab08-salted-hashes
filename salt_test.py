import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "security": "fafa4483874ec051989d53e1e432ba3a6c6b9143",
    "Tomtom": "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2"
}

print("Testing salt:", salt)
print("Hash format: SHA1(salt + password)")
print()

for length in range(5, 8):
    start = 0
    end = 10 ** length

    for number in range(start, end):
        password = str(number).zfill(length)

        test_hash = hashlib.sha1(
            (salt + password).encode()
        ).hexdigest()

        for username, target_hash in targets.items():
            if test_hash == target_hash:
                print("MATCH FOUND")
                print("Username:", username)
                print("Password:", password)
                print("Salt:", salt)
                print("Hash:", test_hash)
                print("-" * 50)
