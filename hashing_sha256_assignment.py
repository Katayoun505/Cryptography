import hashlib

# i. Hash the string "mydata123" using SHA-256
original_string = "mydata123"
hash1 = hashlib.sha256(original_string.encode()).hexdigest()

# ii. Print the original string and its SHA-256 hash
print("Original String:", original_string)
print("SHA-256 Hash of Original String:", hash1)

# iii. Change one character in the string
modified_string = "mydata124"
hash2 = hashlib.sha256(modified_string.encode()).hexdigest()

# iv. Print the modified string and its SHA-256 hash
print("\nModified String:", modified_string)
print("SHA-256 Hash of Modified String:", hash2)

# v. Comment on the observation
print("\nObservation:")
print("Even though we changed only one character, the hash value is completely different.")
print("This shows that SHA-256 is highly sensitive to input changes (avalanche effect).")
