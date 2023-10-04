# morse class to handle translations

class Morse:
    def __init__(self):
        self.morse_dict = {
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

    # methods 
    def validate_char(self, letter):
        """Dictionary lookup to validate input"""
        return letter.upper() in list(self.morse_dict.keys())


    def translate_char(self, letter):
        """Dictionary lookup of character input"""
        return self.morse_dict[letter.upper()]
