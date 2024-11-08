# Caesar Cipher Program in Python

# Function to encrypt the message
def encrypt(message, shift):
    encrypted_message = ""
    
    # Iterate through each character in the message
    for char in message:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around within uppercase ASCII range
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around within lowercase ASCII range
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, add it unchanged
            encrypted_message += char
    
    return encrypted_message

# Function to decrypt the message
def decrypt(message, shift):
    decrypted_message = ""
    
    # Iterate through each character in the message
    for char in message:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character back and wrap around within uppercase ASCII range
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character back and wrap around within lowercase ASCII range
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # If it's not a letter, add it unchanged
            decrypted_message += char
    
    return decrypted_message

# Main function
def main():
    # Ask the user for the message and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    # Ask the user if they want to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

# Run the main function
if __name__ == "__main__":
    main()
