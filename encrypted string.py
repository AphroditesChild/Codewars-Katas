def decrypt(text, n):
    dec = text
    for i in range(n):
        dec = "".join([dec[i+len(dec)//2] + dec[i]  for i in range(len(dec)//2)] + [dec[-1] if len(dec)%2==1 else ""])
    print(dec)

def encrypt(text, n):
    enc = text
    for i in range(n):
        enc = "".join([enc[c] for c in range(1, len(enc), 2)] + [enc[c] for c in range(0, len(enc), 2)])

    print(enc)

encrypt("This is a test!", 1)
decrypt("hsi  etTi sats!", 1)
input()
