from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

# Both encode and decode in a signle function
def caesar(text, shift, direction):
    new_word = ""
    if direction == "decode": shift *= -1
    for letter in text:
        if letter not in alphabet: new_word += letter
        else:
            index = alphabet.index(letter)
            new_word += alphabet[(index + shift) % len(alphabet)]

    return new_word

on = True
while on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(text, shift, direction))

    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == "yes":
        pass
    else:
        on = False