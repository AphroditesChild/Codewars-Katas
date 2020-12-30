def spin_words(sentence):

    LST1 = [list(word) for word in sentence.split()]
    LST2 = [word[::-1] if len(word) >= 5 else word[0::] for word in sentence.split()]
    LST3 = ["".join(revWord) for revWord in LST2]
    print(LST1)
    print(LST2)
    print(LST3)                              # a = [ ['a', 'b', 'c'], ['a', 'b', 'c'], .....     ]                                             #for word in sentence.spli
    print(" ".join([word[::-1] if len(word) >= 5 else word[0::] for word in sentence.split()]))                           #reversed(word.split()) for word in sentence.split())

    #split sentence into words  -> [sentence.split()]
    #iterate through ever word  ->
    #split and reverse    -> reversed([word.split()]) for word in [sentence.split()]
    #join                       -> "".join(reversed([word.split()]))
spin_words("Hello to World")
input()

# return " ".join(["".join(spWrd) for spWrd in [wrd[::-1] if len(wrd) >= 5 else wrd[0::] for wrd in [list(w) for w in sentence.split()]]])
