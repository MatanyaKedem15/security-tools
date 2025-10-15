from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open("private.pem", "wb") as f: f.write(private_key)
    with open("public.pem", "wb") as f: f.write(public_key)
    print("Keys generated: private.pem & public.pem")

def encrypt_message(message):
    public_key = RSA.import_key(open("public.pem").read())
    cipher = PKCS1_OAEP.new(public_key)
    enc = cipher.encrypt(message.encode())
    print("Encrypted (base64):", base64.b64encode(enc).decode())

def decrypt_message(enc_b64):
    private_key = RSA.import_key(open("private.pem").read())
    cipher = PKCS1_OAEP.new(private_key)
    dec = cipher.decrypt(base64.b64decode(enc_b64.encode()))
    print("Decrypted:", dec.decode())

if __name__ == "__main__":
    print("1) Generate keys\n2) Encrypt\n3) Decrypt")
    choice = input("Choose: ")
    if choice == "1":
        generate_keys()
    elif choice == "2":
        msg = input("Enter message: ")
        encrypt_message(msg)
    elif choice == "3":
        msg = input("Enter base64 string: ")
        decrypt_message(msg)
