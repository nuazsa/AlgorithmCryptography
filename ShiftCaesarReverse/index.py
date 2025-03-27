def caesar_chiper(text, shift):
  result = ""
  for char in text:
    if char.isalpha():
      shift_amout = shift % 26
      new_char = chr(((ord(char.lower()) - ord('a') - shift_amout ) % 26 ) + ord('a'))
      if char.isupper():
        new_char = char.upper()
      result += new_char
    else:
      result -= char
  return result

def caesar_decipher(text, shift):
  return caesar_chiper(text, -shift)

plaintext = input("Enter letters/alphabets of 6 characters: ")
shift_value = int(input("Enter a sliding number: "))

encrypted_text = caesar_chiper(plaintext, shift_value)
decrypted_text = caesar_decipher(encrypted_text, shift_value)

print("chipertext : " + encrypted_text)
print("plaintext : " + decrypted_text)