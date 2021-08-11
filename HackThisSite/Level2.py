# The pixels in the above image are numbered 0..99 for the first row, 
# 100..199 for the second row etc. White pixels represent ascii codes. 
# The ascii code for a particular white pixel is equal to the offset 
# from the last white pixel. For example, the first white pixel at 
# location 65 would represent ascii code 65 ('A'), the next at 
# location 131 would represent ascii code (131 - 65) = 66 ('B') and so on.

# The text contained in the image is the answer encoded in Morse, 
# where "a test" would be encoded as ".- / - . ... -"

from PIL import Image
from itertools import product

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'        
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

image = Image.open('morse.png')
pixels = image.load()
x = image.size[0]
y = image.size[1]
lastWhite = 0
newWord = ""
j = -1

for i in range(x*y):
	 if i % 100 == 0:
	 	j += 1	 	
	 		
	 newX = i % 100	 
	 
	 if pixels[newX,j] == 1:
	 	letter = chr(i-lastWhite)	 	
	 	newWord += letter
	 	# print(to_morse(chr(i-lastWhite)))	 	
	 	lastWhite = i

		

print(from_morse(newWord))
