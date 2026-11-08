import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "Sparky":   "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "Mark123":  "92e54f10103a3c511853c7098c04141f114719c1",
    "superman": "437fbc6892b38db6ac5bdbe2eab3f7bc924527d9",
    "security": "fafa4483874ec051989d53e1e432ba3a6c6b9143",
    "Tomtom":   "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2",
    "JillC":    "f44f3b09df53c1c11273def13cacd8922a86d48c"
}

known = {
    "Sparky": "Admin09",
    "Mark123": "Mark123",
    "superman": "qwerty",
    "JillC": "Q2w13sA"
}

for length in range(5, 8):
    for number in range(10 ** length):
        password = str(number).zfill(length)
        h = hashlib.sha1((salt + password).encode()).hexdigest()

        for username in ["security", "Tomtom"]:
            if username not in known and h == targets[username]:
                known[username] = password

print("LAB 08 - FINAL VERIFIED RESULTS")
print("=" * 72)
print("Salt:", salt)
print("Hash construction: SHA1(salt + password)")
print("=" * 72)

for username in targets:
    if username in known:
        password = known[username]
        calculated = hashlib.sha1((salt + password).encode()).hexdigest()
        verified = calculated == targets[username]

        print(f"{username:<10} Password: {password:<10} Verified: {verified}")
    else:
        print(f"{username:<10} Password: NOT RECOVERED")

print("=" * 72)
print("Recovered:", len(known), "out of", len(targets))
