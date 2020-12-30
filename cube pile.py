def find_nb(m):
    n = 0
    sum = 0
    while sum != m :
        sum += (n+1)**3
        n+=1
        print(sum)
        if sum == m : return n
        if sum > m : return -1


print(find_nb(156487))
input()
