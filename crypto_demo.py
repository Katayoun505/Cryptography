from cryptography.fernet import Fernet
import hashlib

key = Fernet.generate_key()
cipher = Fernet(key)

message = "Confidential message"
encoded_message = message.encode()

encrypted_message = cipher.encrypt(encoded_message)
print("[ENCRYPTED] Encrypted message:", encrypted_message)

decrypted_message = cipher.decrypt(encrypted_message)
print("[DECRYPTED] Decrypted message:", decrypted_message.decode())

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_hash = hash_password("my_secure_password")

def verify_password(input_password):
    input_hash = hash_password(input_password)
    if input_hash == stored_hash:
        print("[PASS] Password match. Access granted.")
    else:
        print("[FAIL] Incorrect password. Access denied.")

verify_password("my_secure_password")
verify_password("wrong_password")
   
