def mix(s1,s2):
    d1 = {letter: s1.count(letter) for letter in s1 if letter in 'abcdefghijklmnopqrstuvwxyz' and s1.count(letter) > 1}
    d2 = {letter: s2.count(letter) for letter in s2 if letter in 'abcdefghijklmnopqrstuvwxyz' and s2.count(letter) > 1}
    differences = []
    for k in set(list(d1.keys())+list(d2.keys())):
        if d1.get(k, 0) > d2.get(k, 0):
            differences.append("1:" + k*d1[k])
        elif d2.get(k, 0) > d1.get(k, 0):
            differences.append("2:" + k*d2[k])
        else :
            differences.append("=:" + k*d1[k])


    return "/".join(sorted(differences, key=lambda i: (len(i), -ord(i[0]), -ord(i[-1])), reverse=True))

print(mix("Are they here", "yes, they are here"))

input()
