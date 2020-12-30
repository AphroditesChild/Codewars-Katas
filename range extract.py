def solution(args):
    print(args)
    newargs = []
    i = 0
    while i < len(args):
        j = i
        rng = 0
        while j < len(args)-1:
            if args[j+1] == args[j]+1:
                rng += 1
                j += 1
            else : break
        if rng >= 2 :
            newargs.append("{}-{}".format(args[i], args[i+rng]))
            i += rng+1
        else :
            newargs.append(str(args[i]))
            i += 1
    return ",".join(newargs)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
input()
