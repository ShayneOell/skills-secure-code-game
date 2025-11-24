# Welcome to Secure Code Game Season-1/Level-5!

import binascii
import secrets
import hashlib
import os
import bcrypt

class Random_generator:

    # cryptographically safe token generator
    def generate_token(self, length=8, alphabet=(
        '0123456789'
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    # secure, correctly generated bcrypt salt
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)


class SHA256_hasher:

    # secure password hashing: bcrypt(password || sha256(password))
    def password_hash(self, password, salt):
        # Hash with SHA256 first
        sha256_pw = hashlib.sha256(password.encode()).digest()

        # Let bcrypt handle the full hash securely
        password_hash = bcrypt.hashpw(sha256_pw, salt)

        return password_hash.decode('utf-8')

    def password_verification(self, password, password_hash):
        sha256_pw = hashlib.sha256(password.encode()).digest()
        return bcrypt.checkpw(sha256_pw, password_hash.encode('utf-8'))


class MD5_hasher:

    # MD5 is insecure — replace it with SHA256
    # Keep class name for compatibility, upgrade underlying hashing
    def password_hash(self, password):
        # strong hash instead of MD5
        return hashlib.sha256(password.encode()).hexdigest()

    def password_verification(self, password, password_hash):
        computed = self.password_hash(password)
        # constant‑time comparison
        return secrets.compare_digest(computed, password_hash)



PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY  = os.environ.get("PUBLIC_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
PASSWORD_HASHER = "SHA256_hasher"
