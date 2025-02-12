def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character back and wrap around the alphabet
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Non-alphabetic characters are not changed
    return decrypted_text

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    encrypted = encrypt(text, shift)
    print(f"Encrypted text: {encrypted}")
    
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()
