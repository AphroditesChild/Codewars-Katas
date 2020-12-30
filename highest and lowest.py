def high_and_low(stg):
    lst = stg.split()
    largest = int(lst[0])
    smallest = int(lst[0])
    for i in lst :
        if int(i) > largest :
            largest = int(i)
        if int(i) < smallest :
            smallest = int(i)
    res = str(largest) + ' ' + str(smallest)
    print(res)

a = "1 54 0 -245 44 32 -1 -48 123"

high_and_low(a)

input()
