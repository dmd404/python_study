from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            original = alphabet.index(letter)
            new_position = (original + shift_amount) % 26
            final_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f'The {cipher_direction}d text is {final_text}')

print(logo)

rerun = True
while rerun:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  user_rerun = input('continue? ').lower()
  if user_rerun == 'no':
    rerun = False
    print('Bye')
