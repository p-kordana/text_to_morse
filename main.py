# App Name: text_to_morse
# App Author: Paul Kordana
# App Description: simple python script to translate user input text into morse code representation

# imports
from morse import Morse

# instantiate
m = Morse()

# welcome message
print("This program will take your text input and translate it into morse code.")

# gather user input
text_input = input("Enter text to translate: ")

# init output var
morse_output = ""

# validate/translate each letter and concat to output var
for c in text_input:
    if m.validate_char(c):
        morse_output += m.translate_char(c)
    else:
        morse_output += c
    morse_output += ' '

# print translated text to console
print(morse_output)
