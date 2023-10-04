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
    def translate_word(self, word):
        """Dictionary lookup of character input"""

        # init output var
        output = ""

        # loop letters and validate they exist in the dictionary
        for letter in word:
            # convert to upper to match dictionary keys
            if letter.upper() in list(self.morse_dict.keys()):
                output += self.morse_dict[letter.upper()]
            else:
                output += letter
            # add blank space between letters
            output += ' '

        return output
