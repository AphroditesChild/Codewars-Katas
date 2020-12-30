def digital_root(x):
    root = x
    while root > 9 :
        sum = 0
        for i in range(len(str(root))) :
            sum += (root // 10**i) % 10
        root = sum
    return root

print(digital_root(5468))
input()
