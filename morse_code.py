MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter.upper() in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        elif letter == ' ':
            cipher += ' '
        else:
            raise ValueError("Invalid character for encryption: '{}'".format(letter))

    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:

        if letter != ' ':
            i = 0
            citext += letter

        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                try:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                   .values()).index(citext)]
                    citext = ''
                except ValueError:
                    raise ValueError("Invalid Morse code: '{}'".format(citext))

    return decipher


def main():
    user_input = input("Enter text: ")
    choice = input("Encrypt or Decrypt? (E/D): ")

    if choice.upper() == 'E':
        try:
            result = encrypt(user_input)
            print("Encrypted message:", result)
        except ValueError as e:
            print("Error:", e)
    elif choice.upper() == 'D':
        try:
            result = decrypt(user_input)
            print("Decrypted message:", result)
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")


if __name__ == '__main__':
    main()
