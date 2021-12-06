import pyperclip as pc
def greet():
    print("""
          ___                             ___          _            
         / __|___ __ _ ___ __ _ _ _ ___  / __|  _ _ __| |_  ___ _ _ 
        | (__/ -_) _` (_-</ _` | '_(_-< | (_| || | '_ \ ' \/ -_) '_|
         \___\___\__,_/__/\__,_|_| /__/  \___\_, | .__/_||_\___|_|  
                                             |__/|_|    
          """)
greet()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]
direction = input("Type \'encode\' to encode a message or type \'decode\' to decode a message: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type your shift number:\n"))

def encrypt(plainText, shiftAmmount):
    cypherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmmount
        newLetter = alphabet[newPosition]
        cypherText += newLetter
    print(f"The encoded message is: {cypherText}\nEncoding copied to clipboard")
    pc.copy(cypherText)
    
def decrypt(cypherText, shiftAmmount):
    plainText = ""
    for letter in cypherText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmmount
        plainText += alphabet[newPosition]
    print(f"The decoded message is: {plainText}")

if direction == "encode":
    encrypt(plainText=text, shiftAmmount=shift)
elif direction == "decode":
    decrypt(cypherText=text, shiftAmmount=shift)
else:
    print("Invalid Option: Exiting")