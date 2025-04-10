def caesar_cipher(text, shift):
  result = ""
  for char in text:
    if char.isalpha():
      shift_base = ord('A') if char.isupper() else ord('a')
      result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
    else:
      result += char
  return result

def double_caesar_encrypt(text, shift1, shift2):
  step1 = caesar_cipher(text, shift1)
  step2 = caesar_cipher(step1, shift2)
  return step2

def double_caesar_decrypt(text, shift1, shift2):
  step1 = caesar_cipher(text, -shift2)
  step2 = caesar_cipher(step1, -shift1)
  return step2

plain_text = input("Enter letters/alphabets of 6 characters: ")
shift1 = int(input("Enter a sliding number Key 1: "))
shift2 = int(input("Enter a sliding number Key 2: "))

encrypted_text = double_caesar_encrypt(plain_text, shift1, shift2)
print("chipertext:", encrypted_text)
ver
decrypted_text = double_caesar_decrypt(encrypted_text, shift1, shift2)
print("plaintext:", decrypted_text)