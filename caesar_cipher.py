def caesar_cipher(text, shift=3, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

if __name__ == "__main__":
    msg = input("Enter text: ")
    shift = int(input("Shift (e.g., 3): "))
    mode = input("Encrypt (e) or Decrypt (d)? ").lower()
    print(caesar_cipher(msg, shift, decrypt=(mode == 'd')))
