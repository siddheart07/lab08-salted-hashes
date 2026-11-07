import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "security": "fafa4483874ec051989d53e1e432ba3a6c6b9143",
    "Tomtom": "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2"
}

found = {}

for length in range(5, 8):
    for number in range(10 ** length):
        password = str(number).zfill(length)
        test_hash = hashlib.sha1((salt + password).encode()).hexdigest()

        for username, target_hash in targets.items():
            if username not in found and test_hash == target_hash:
                found[username] = password

print("LAB 08 - NUMERIC PASSWORD RESULTS")
print("=" * 45)

for username, password in found.items():
    verify_hash = hashlib.sha1((salt + password).encode()).hexdigest()

    print("Username :", username)
    print("Password :", password)
    print("Salt     :", salt)
    print("SHA1     :", verify_hash)
    print("Verified :", verify_hash == targets[username])
    print("-" * 45)
