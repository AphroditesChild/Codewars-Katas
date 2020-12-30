import math

def nextPerfectSquare(N):
    if (math.sqrt(N)).is_integer() == False :
        return -1
    else :
        return pow(int(math.sqrt(N))+1, 2)

inp = input("Enter a number : ")
num = int(inp)
print(nextPerfectSquare(num))

input()
