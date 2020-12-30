import string


def is_pangram(inp) :
    alphabet = {}
    for i in range(97, 123) :
        alphabet[chr(i)] = alphabet.get(chr(i), 0)
    for c in inp :
        if ord(c.lower()) in range(97, 123) :
            alphabet[c.lower()] = 1
    for letter in alphabet :
        if alphabet[letter] == 0 :
            return False
    return True


sentence = input("Type a sentence : ")

print(is_pangram(sentence))

input()
