alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  encrypted_txt = ""
  for letter in plain_text:
    original = alphabet.index(letter)
    new_position = (original + shift_amount) % 26  # in case index runs out of range
    new_letter = alphabet[new_position]
    encrypted_txt += new_letter
  
  print(encrypted_txt)

# Create a decrypt function 
def decrypt(encrypted_text, shift_amount):
  decrypted_txt = ""
  # shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  for letter in encrypted_text:
    position = alphabet.index(letter)
    new_position = (position - shift_amount) % 26
    decrypted_txt += alphabet[new_position]
  print(decrypted_txt)
  

# Check if the user wanted to encrypt or decrypt the message 
if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)
                           
