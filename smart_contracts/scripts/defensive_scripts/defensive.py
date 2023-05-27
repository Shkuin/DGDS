from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import secrets


def generate_secret_key(bytes):
    return secrets.token_bytes(bytes)


def encrypt_AES(key, plaintext):
    # Convert key and plaintext to bytes if necessary
    if isinstance(key, str):
        key = key.encode()
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()

    # Generate a random initialization vector (IV) for CBC mode
    iv = default_backend().randomized_read(algorithms.AES.block_size // 8)

    # Create an AES-CBC cipher with the specified key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Encrypt the plaintext using the cipher and return the ciphertext and IV
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext, iv


def decrypt_AES(key, ciphertext, iv):
    # Convert key, ciphertext, and IV to bytes if necessary
    if isinstance(key, str):
        key = key.encode()
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode()
    if isinstance(iv, str):
        iv = iv.encode()

    # Create an AES-CBC cipher with the specified key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Decrypt the ciphertext using the cipher and return the plaintext
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()


def split_func(ipfs_hash):
    firstpart, secondpart = (
        ipfs_hash[: len(ipfs_hash) // 2],
        ipfs_hash[len(ipfs_hash) // 2 :],
    )
    return firstpart, secondpart
