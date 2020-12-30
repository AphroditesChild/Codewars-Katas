def longest_repetition(chars) :
    if chars == '' : return ('', 0)
    lst = []
    count = []
    n = 1
    for i in range(len(chars)-1) :
        if chars[i+1] == chars[i] :
            n += 1
            continue
        else :
            lst.append(chars[i])
            count.append(n)
            n = 1
            continue
    if chars[len(chars)-1] != chars[len(chars)-2] :
        lst.append(chars[len(chars)-1])
        count.append(1)
    else :
        lst.append(chars[len(chars)-1])
        count.append(n)
    big = 0
    i = 0
    for i in range(len(count)) :
        if count[i] > big :
            big = count[i]
            ind = i
    return (lst[ind], big)

st = 'abbbbb'
print(longest_repetition(st))

input()
