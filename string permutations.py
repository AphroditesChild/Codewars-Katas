from itertools import permutations as perm

def permutations(string):
    return ["".join(p) for p in set(perm(string))]


print(permutations("aabbjtgezryty"))
input()
