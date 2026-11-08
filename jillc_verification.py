import hashlib

salt = "www.exploringsecurity.com"
password = "Q2w13sA"
target = "f44f3b09df53c1c11273def13cacd8922a86d48c"

calculated = hashlib.sha1((salt + password).encode()).hexdigest()

print("Username : JillC")
print("Password :", password)
print("Salt     :", salt)
print("SHA1     :", calculated)
print("Verified :", calculated == target)
