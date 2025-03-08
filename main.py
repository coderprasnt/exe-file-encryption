
# Please Buy the working script- This is only a simulation!
#Telegram- @witchshophub

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_file(file_path, key):
    output_file = file_path + ".enc"
    with open(file_path, 'rb') as f:
        data = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphertext)
    
    print(f"🔐 Encrypted file saved as: {output_file}")

def decrypt_file(enc_file_path, key):
    output_file = enc_file_path.replace(".enc", ".dec.exe")
    with open(enc_file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    with open(output_file, 'wb') as f:
        f.write(data)
    
    print(f"🔓 Decrypted file saved as: {output_file}")

if __name__ == "__main__":
    key = os.urandom(16)  # Generate a random 16-byte key
    file_path = input("Enter the path of the EXE file to encrypt: ")
    
    encrypt_file(file_path, key)
    
    # Decryption for testing purposes
    enc_file_path = file_path + ".enc"
    decrypt_file(enc_file_path, key)
