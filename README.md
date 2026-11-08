# Lab 08 – Salted Hashes

**Module:** Secure Communication and Cryptography  
**Challenge:** Lab 08 – Salted Hashes  
**Team:** Ram Siddharth Ramasamy Raja and Jeyanth Kannan  
**Purpose:** Educational password-hash analysis and recovery exercise based on the supplied university lab dataset.

## Case summary

The supplied database dump contained six salted password hashes. The lab clues indicated that:

- all passwords used the same salt,
- the salt value appeared in the supplied case information,
- passwords before the May 2010 policy change were numeric and 5–7 characters long,
- newer passwords were alphanumeric and 5–7 characters long,
- the site domain was `www.exploringsecurity.com`,
- captured code suggested a construction of the form `CommonHash($salt,$pass)`.

## Confirmed hash construction

The recovered results confirmed the effective construction used in the lab:

```text
SHA1(salt + password)
```

with:

```text
salt = www.exploringsecurity.com
```

## Verified results

| Username | Recovered password | Status |
|---|---|---|
| Sparky | Admin09 | Verified |
| Mark123 | Mark123 | Verified |
| superman | qwerty | Verified |
| security | 121298 | Verified |
| Tomtom | 54321 | Verified |
| JillC | Q2w13sA | Verified |

**Recovered:** 6 out of 6 accounts.

Each recovered password was verified by recomputing `SHA1(salt + password)` and comparing the digest with the original database hash.

## Investigation approach

1. Extract the username/hash pairs.
2. Check the hash length and hexadecimal format.
3. Test the suspected common salt from the case information.
4. Recover older numeric passwords by brute force.
5. Filter a dictionary to 5–7 character alphanumeric candidates.
6. Try username mutations and word+number combinations.
7. Use John the Ripper rule and mask attacks for remaining accounts.
8. Recover Sparky with the seven-character mask `?u?l?l?l?l?d?d`.
9. Recover JillC with a targeted seven-character mask and verify the result.
10. Independently verify all recovered passwords.

## Files

- `hash_type_check.py` – checks hash length and hexadecimal structure.
- `salt_test.py` – tests the suspected salt and recovers older numeric passwords.
- `numeric_results.py` – verifies the two recovered numeric passwords.
- `alphanumeric_dictionary.py` – dictionary attack against the newer alphanumeric accounts.
- `username_mutation_attack.py` – targeted username-derived mutations.
- `word_number_attack.py` – word-plus-number candidate generation.
- `final_results.py` – final independent verification and summary.
- `hashes.txt` – original username/hash pairs from the lab dataset.
- `remaining_john.txt` – John the Ripper input for Sparky and JillC.
- `jillc_only.txt` – John the Ripper input used for the JillC mask attack.
- `jillc_verification.py` – independently verifies JillC's recovered password.

## Security observations

The exercise demonstrates that a salt does not prevent offline guessing when the salt and hash construction are known. Reusing the same salt across accounts is weaker than using a unique random salt per password. SHA-1 is also too fast for modern password storage; dedicated password-hashing functions such as Argon2id, bcrypt, scrypt or PBKDF2 are more appropriate.

This repository contains only the code and lab dataset values required to reproduce the university exercise.
