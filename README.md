# 🔐 Security Tools

A lightweight **Python toolkit** for basic security operations — hashing, encryption, and decryption.  
Built to demonstrate knowledge of cryptography fundamentals and practical Python scripting for backend and security engineering tasks.

---

## 🚀 Features
- Compute **SHA256** or **MD5** hash of any file.  
- Perform **Caesar cipher** encryption and decryption.  
- Generate **RSA key pairs**, encrypt, and decrypt messages.  
- Clean CLI interface for quick use and testing.  

---

## 📂 Project Structure
```
security-tools/
│
├── hash_util.py # Compute file hashes (MD5, SHA256)
├── caesar_cipher.py # Caesar cipher encryption/decryption
├── rsa_tool.py # RSA key generation & message encryption/decryption
├── requirements.txt # Dependencies
└── README.md
```

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** hashlib, pycryptodome  
- **Concepts:** Hashing, Symmetric & Asymmetric Encryption, CLI tools  

---

## ⚙️ Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/security-tools.git
   cd security-tools
   ```
2. Install dependencies:
```
pip install -r requirements.txt
```
▶️ How to Run

1️⃣ Hashing Utility

Compute the SHA256 or MD5 hash of any file.
```
python hash_util.py myfile.txt sha256
```
If no algorithm is provided, defaults to SHA256.


2️⃣ Caesar Cipher

Encrypt or decrypt text using a simple letter-shifting cipher.
```
python caesar_cipher.py
```
Follow the interactive prompts:
```
Enter text: hello
Shift (e.g., 3): 3
Encrypt (e) or Decrypt (d)? e
Result: khoor
```
3️⃣ RSA Encryption Tool

Generate RSA keys, encrypt, and decrypt messages.

Generate keys:
```
python rsa_tool.py
# Select option 1
```
Encrypt a message:
```
python rsa_tool.py
# Select option 2
```
Decrypt a message:
```
python rsa_tool.py
# Select option 3
```
This will create:
```
private.pem
public.pem
```
📦 requirements.txt
```
pycryptodome
```
🧪 Example Output
SHA256 Hash
```
SHA256 hash for sample.txt:
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
```
Caesar Cipher
```
Enter text: hello world
Shift: 4
Result: lipps asvph
```
RSA
```
Keys generated: private.pem & public.pem
Encrypted (base64): YXNkZmFzZGZhc2RmYXNkZg==
Decrypted: my secret text
```
## 👤 Author
**Matanya Kedem**

[LinkedIn](https://www.linkedin.com/in/USERNAME) • [GitHub](https://github.com/USERNAME)

