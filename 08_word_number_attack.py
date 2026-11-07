import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c"
}

found = {}

def check(password):
    h = hashlib.sha1((salt + password).encode()).hexdigest()

    for username, target in targets.items():
        if username not in found and h == target:
            found[username] = password

            print("MATCH FOUND")
            print("Username :", username)
            print("Password :", password)
            print("Hash     :", h)
            print("-" * 50)

            return True

    return False

print("LAB 08 - WORD + NUMBER TARGETED ATTACK")
print("=" * 55)

words = []

with open("rockyou.txt", "r", errors="ignore") as f:
    for line in f:
        word = line.strip()

        if word.isalpha() and 3 <= len(word) <= 6:
            words.append(word)

        if len(words) >= 50000:
            break

print("Base words loaded:", len(words))
print("Testing word + number combinations...")
print()

for word in words:
    variants = {
        word.lower(),
        word.capitalize(),
        word.upper()
    }

    for base in variants:
        if 5 <= len(base) <= 7:
            check(base)

        for n in range(100):
            num = str(n)

            candidates = [
                base + num,
                num + base
            ]

            for password in candidates:
                if 5 <= len(password) <= 7:
                    check(password)

        if len(found) == len(targets):
            break

    if len(found) == len(targets):
        break

print()
print("=" * 55)
print("Recovered:", len(found), "out of", len(targets))

if len(found) < len(targets):
    print("Still remaining:")

    for username in targets:
        if username not in found:
            print("-", username)
