def anagrams(word, words):
    return [w for w in words if "".join(sorted(w))=="".join(sorted(word))]




print(anagrams('sefg', ['aabb', 'abcd', 'bbaa', 'dada']))

input()
