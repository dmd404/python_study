alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'plain_text' and 'shift_amount' as inputs.
def encrypt(plain_text, shift_amount):
  # shift each letter of the 'plain_text' forwards in the alphabet by the 'shift_amount' and print the encrypted text
  encrypted_txt = ""
  for letter in plain_text:
    original = alphabet.index(letter)
    new_position = (original + shift_amount) % 26  # in case index runs out of range
    new_letter = alphabet[new_position]
    encrypted_txt += new_letter
  
  print(encrypted_txt)

encrypt(text, shift)
                           
