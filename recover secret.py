def recoverSecret(triplets):
    secret = []
    for triplet in triplets:
        for letter in triplet:
            if letter not in secret:
                secret += letter
    print(secret)
    for triplet in triplets :
        for i in range(2):
            if secret.index(triplet[i]) > secret.index(triplet[i+1]):
                secret.insert(secret.index(triplet[i+1]), secret.pop(secret.index(triplet[i])))
                print(secret)
    return secret

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))
input()
