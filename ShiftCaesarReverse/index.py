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

# Contoh penggunaan
plaintext = input("Masukan huruf/abjad sebanyak 6 karakter: ")
shift_value = int(input("Masukkan angka geser: "))

print("chipertext : " + caesar_chiper(plaintext, shift_value))
print("plaintext : " + caesar_chiper(plaintext, shift_value))