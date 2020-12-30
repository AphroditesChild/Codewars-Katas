MORSE_CODE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', 'SOS':'...---...', '!':'-.-.--'}
REVERSE_CODE = {v:k for k,v in MORSE_CODE.items()}

def decodeMorse(morse_code):

    return " ".join( ["".join(decLetterLst) for decLetterLst in [[REVERSE_CODE[encLetter] for encLetter in encLetterLst]
                          for encLetterLst in [encWrdStr.split() for encWrdStr in morse_code.split("   ")]  ]  ] )

print(decodeMorse(input("ENTER MSG:  ")))
input()
