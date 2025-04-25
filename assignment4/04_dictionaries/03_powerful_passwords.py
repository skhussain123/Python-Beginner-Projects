import hashlib


def hash_password(password: str) -> str:
    """Returns the SHA256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("securePassword!"),
}

def login(email: str, password_to_check: str) -> bool:
    """Returns True if the hashed password matches the stored hashed password."""

    if email in stored_logins:
        stored_hash = stored_logins[email]
        
        if hash_password(password_to_check) == stored_hash:
            return True
    
    return False

email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password):
    print("Login successful!")
else:
    print("Invalid email or password.")
