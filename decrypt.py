"""
    usage python decrypt.py <folder/file> <folder/file path>
    eg: python decrypt.py folder ./data>
"""

from cryptography.fernet import Fernet
from pathlib import Path
import sys
 
n = len(sys.argv)
path_to_key='key.key'

if n!=3:
    raise Exception("check usage")

def decrypt(filepath):
    
    with open(path_to_key, 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)

    # opening the encrypted file
    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    
    # opening the file in write mode and
    # writing the decrypted data
    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)

def main():
    if sys.argv[1]=="folder":
        files = Path(sys.argv[2]).glob('*')
        for file in files:
            decrypt(file)
    if sys.argv[1]=="file":
        decrypt(sys.argv[2])

main()