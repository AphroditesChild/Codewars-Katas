def is_interesting(number, awesome_phrases):
    a2 = number > 99
    a1 = number + 1 > 99 or number +2 > 99

    b2 = set(str(number)[1:]).issubset({'0'})
    b1 = set(str(number+1)[1:]).issubset({'0'}) or set(str(number+2)[1:]).issubset({'0'})

    c2 = str(number) in "0123456789" or str(number) in "9876543210"
    c1 = str(number+1) in "1234567890" or str(number+1) in "9876543210" or str(number+2) in "1234567890" or str(number+2) in "9876543210"

    d2 = str(number) == str(number)[::-1]
    d1 = str(number+1) == str(number+1)[::-1] or str(number+2) == str(number+2)[::-1]

    e2 = number in awesome_phrases
    e1 = number+1 in awesome_phrases or number+2 in awesome_phrases

    if a2 and (b2 or c2 or d2 or e2): return 2
    elif a1 and(b1 or c1 or d1 or e1): return 1
    else : return 0

print(is_interesting(8999, [1337,256]))
input()
