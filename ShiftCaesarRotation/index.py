def caesar_multi_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key[i % key_length]
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text
 
def caesar_multi_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key[i % key_length]
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
 
text = input("Enter letters/alphabets of 6 characters: ")
key_input = input("Enter a sliding number (separate with space, ex: 3 1 4 2): ")

key = list(map(int, key_input.split()))

encrypted = caesar_multi_encrypt(text, key)
decrypted = caesar_multi_decrypt(encrypted, key)

print("\nplaintext :", text)
print("chipertext:", encrypted)
print("plaintext :", decrypted)