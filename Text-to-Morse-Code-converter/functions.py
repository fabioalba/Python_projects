

def encode(message, alphabet):
    ''' encodes a text message in morse language '''
    morse_msg = "/"
    for letter in message:
        if letter in alphabet:
            morse_msg += f"{alphabet[letter]}/"
        else:
            morse_msg += f"{letter}/"
    print(f"message in morse code: {morse_msg}")
    return morse_msg

def decode(message, alphabet):
    ''' translates a morse-coded message to text '''

    letter = ""
    decoded_msg = ""
    for i in range(1, len(message)):
        char = message[i]
        if char != "/":
            letter += char
        elif char == "/":
            if letter in alphabet:
                decoded_msg += alphabet[letter]
            else:
                decoded_msg += letter
            letter = ""
    print(f"decoded message: {decoded_msg}")








