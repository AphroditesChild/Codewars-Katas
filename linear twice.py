def dbl_linear(n) :
    y = 0
    z = 0
	u = [1]
    while len(u)<=n :
        a = 2*list[y] + 1
        b = 3*list[z] + 1
        if a<b :
            u.append(a)
            y += 1
        elif a>b :
            u.append(b)
            z += 1
        else :
            u.append(a)
            y += 1
            z += 1

    return u[n]

print(dbl_linear(20))
input()
