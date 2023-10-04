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

# print translated text to console
print(m.translate_word(text_input))
