def CaesarCipher(text, shift):
    s = int(shift)
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


text = input("Please enter the text: ")
shift = int(input("Please enter how many digits to shift: "))
print(CaesarCipher(text, shift))
