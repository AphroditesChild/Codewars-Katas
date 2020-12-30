def rot13(message):
    return "".join([chr(ord(i)+13) if ord(i.lower()) in range(97,110) else chr(ord(i)-13) if ord(i.lower()) in range(110,123) else i for i in message])

print(rot13("Barra Nik Ommek"))
input()
