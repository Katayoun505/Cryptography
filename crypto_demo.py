from cryptography.fernet import Fernet
import hashlib

# ------------------------
# Part 1: Symmetric Encryption
# ------------------------

# Generate a secret key for Fernet (AES-based)
key = Fernet.generate_key()
cipher = Fernet(key)

# Original message to encrypt
message = "Confidential message"
encoded_message = message.encode()

# Encrypt the message
encrypted_message = cipher.encrypt(encoded_message)
print("[ENCRYPTED] Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print("[DECRYPTED] Decrypted message:", decrypted_message.decode())

# ------------------------
# Part 2: Hashing for Password Storage
# ------------------------

# Function to hash passwords using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Store the hash of the real password (this would be saved in a real system)
stored_hash = hash_password("my_secure_password")

# Function to verify password entered by the user
def verify_password(input_password):
    input_hash = hash_password(input_password)
    if input_hash == stored_hash:
        print("[PASS] Password match. Access granted.")
    else:
        print("[FAIL] Incorrect password. Access denied.")

# ------------------------
# Part 3: Test the Login System
# ------------------------

# Test with correct password
verify_password("my_secure_password")  # Should pass

# Test with incorrect password
verify_password("wrong_password")      # Should fail
