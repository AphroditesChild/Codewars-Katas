def valid_parentheses(string):
    s = "".join([p for p in string if p in '()'])

    while len(s) > 0 :
        s = s.split('()')
        s = "".join(s)
        if s == "".join(s.split("()")) : break

    return len(s)==0

print(valid_parentheses("dsf(ffg)()sd"))
input()
