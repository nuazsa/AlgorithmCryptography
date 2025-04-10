import random
import string

def generate_random_alphabet(): 
  original = list(string.ascii_uppercase) 
  shuffled = original[:]
  random.shuffle(shuffled)
  return dict(zip(original, shuffled)), dict(zip(shuffled, original))

def encrypt(text, cipher_map):
  text = text.upper() 
  return "".join(cipher_map.get(char, char) for char in text)

def decrypt(encrypted_text, decipher_map): 
  return "".join(decipher_map.get(char, char) for char in encrypted_text)

cipher_map, decipher_map = generate_random_alphabet() 
plaintext = "HELLO WORLD" 
encrypted_text = encrypt(plaintext, cipher_map) 
decrypted_text = decrypt(encrypted_text, decipher_map)

print(f"Plaintext: {plaintext}") 
print(f"Encrypted: {encrypted_text}") 
print(f"Decrypted: {decrypted_text}")