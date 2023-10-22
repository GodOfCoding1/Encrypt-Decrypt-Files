"""
    usage python encrypt.py <folder/file> <folder/file path>
    eg: python encrypt.py folder ./data
    eg: python encrypt.py folder ./data
"""
from cryptography.fernet import Fernet
from pathlib import Path
import sys

n = len(sys.argv)
path_to_key='key.key'
data_directory="./data"

if n!=3:
    raise Exception("check usage")

def encrypt(filepath):
    with open(path_to_key, 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(filepath, 'rb') as file:
        original = file.read()
    # encrypting the file
    encrypted = fernet.encrypt(original)
    # opening the file in write mode and 
    # writing the encrypted data
    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def main():
    if sys.argv[1]=="folder":
        files = Path(sys.argv[2]).glob('*')
        for file in files:
            encrypt(file)
    if sys.argv[1]=="file":
        encrypt(sys.argv[2])

main()