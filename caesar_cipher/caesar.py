alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  final_text = ""
  for letter in start_text:
    original = alphabet.index(letter)
    if direction == 'decode':
      shift_amount *= -1
    new_position = (original + shift_amount) % 26
    final_text += alphabet[new_position]
    
  print(f'The {cipher_direction}d text is {final_text}')

caesar(text, shift, direction)
