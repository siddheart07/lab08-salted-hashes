import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c"
}

bases = {
    "Sparky": ["Sparky", "sparky", "SPARKY"],
    "JillC": ["JillC", "jillc", "JILLC", "Jillc", "jillC"]
}

def check(username, password):
    test_hash = hashlib.sha1((salt + password).encode()).hexdigest()

    if test_hash == targets[username]:
        print("MATCH FOUND")
        print("Username :", username)
        print("Password :", password)
        print("Hash     :", test_hash)
        print("-" * 50)
        return True

    return False

print("LAB 08 - USERNAME MUTATION ATTACK")
print("=" * 50)

for username, base_list in bases.items():
    found = False

    for base in base_list:
        candidates = set()

        candidates.add(base)
        candidates.add(base[::-1])

        for n in range(100):
            candidates.add(base + str(n))
            candidates.add(str(n) + base)

        replacements = {
            "a": ["4"],
            "e": ["3"],
            "i": ["1"],
            "l": ["1"],
            "o": ["0"],
            "s": ["5"]
        }

        for i, char in enumerate(base):
            lower = char.lower()

            if lower in replacements:
                for replacement in replacements[lower]:
                    modified = base[:i] + replacement + base[i+1:]
                    candidates.add(modified)

        for password in candidates:
            if 5 <= len(password) <= 7 and password.isalnum():
                if check(username, password):
                    found = True
                    break

        if found:
            break

    if not found:
        print(username, ": no match found with username mutations")
