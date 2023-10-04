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


# welcome message
print("This program will take your text input and translate it into morse code.")
print(list(MORSE_DICT.keys()))
# gather user input
text_input = input("Enter text to translate: ")
while text_input not in list(MORSE_DICT.keys()):
    text_input = input("Enter text to translate: ")

# init output var
morse_output = ""

# translate each letter
for c in text_input:
    pass