alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from logo import display

print(display)
direction = input("You want to 'encode' or 'decode' your message ?\n")
text = input("Type your message:\n").lower()

def encrypt(plain_text):
  message = ""
  end_num = ""

  #char = ""
  
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + 3
      #message += alphabet[new_position]
      end_num += alphabet[new_position]
    else:
      end_num += letter
  print(f"The encoded text is {message}{end_num}")


def decrypt(message):

  plain_text = ""
  for letter in message:
    position = alphabet.index(letter)
    new_position = position - 3
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#Called function to either encode or decode
if direction == "encode":
  encrypt(plain_text=text)
elif direction == "decode":
  decrypt(message=text)