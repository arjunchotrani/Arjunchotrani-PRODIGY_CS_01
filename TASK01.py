def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer!")
        return

    if choice == 'encrypt':
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'decrypt':
        result = caesar_decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
