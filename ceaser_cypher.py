from ceaser_cypher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"[+] Here's the {cipher_direction}d result: {end_text}")

def play():
    text = input("[+] Type your message:").lower()
    shift = int(input("[+] Type the shift number:"))
    direction = input("[+] Type 'encode' to encrypt, type 'decode' to decrypt:").lower()

    while True:
        if shift > 26:
            shift %= 26
        else:
            break

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

print(logo)
play()
while True:
    user_choice = input("[+] Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if user_choice == "yes" or user_choice == "y":
        play()
    elif user_choice == "no" or user_choice == "n" :
        print("[-] Thank you for the game.")
        break
