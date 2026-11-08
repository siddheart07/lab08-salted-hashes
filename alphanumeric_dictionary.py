import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "Mark123": "92e54f10103a3c511853c7098c04141f114719c1",
    "superman": "437fbc6892b38db6ac5bdbe2eab3f7bc924527d9",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c"
}

found = {}

print("LAB 08 - ALPHANUMERIC DICTIONARY ATTACK")
print("Salt:", salt)
print("Format: SHA1(salt + password)")
print("-" * 55)

with open("05_candidates_5_7.txt", "r", errors="ignore") as f:
    for line in f:
        password = line.strip()

        test_hash = hashlib.sha1(
            (salt + password).encode()
        ).hexdigest()

        for username, target in targets.items():
            if username not in found and test_hash == target:
                found[username] = password
                print("MATCH FOUND")
                print("Username :", username)
                print("Password :", password)
                print("Hash     :", test_hash)
                print("-" * 55)

print()
print("Recovered:", len(found), "out of", len(targets))

if len(found) < len(targets):
    print("Remaining accounts:")
    for username in targets:
        if username not in found:
            print("-", username)
