MORSE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
}

def validate_char(letter):
    """Dictionary lookup to validate input"""
    return letter.upper() in list(MORSE_DICT.keys())


def translate_char(letter):
    """Dictionary lookup of character input"""
    return MORSE_DICT[letter.upper()]

# welcome message
print("This program will take your text input and translate it into morse code.")

# gather user input
text_input = input("Enter text to translate: ")

# init output var
morse_output = ""

# translate each letter
for c in text_input:
    if validate_char(c):
        morse_output += translate_char(c)
    else:
        morse_output += c

print(morse_output)