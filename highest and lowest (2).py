def high_and_low(numbers):
    # numbers.split() returns a list containing each element of numbers within a space from the other
    # nn is a list containing elements of number converted into numbers(int)
    nn = [int(s) for s in numbers.split(" ")]
    print("%i %i" % (max(nn),min(nn)))
    # the function will return a string containing the biggest and the smallest elements of nn separated with a space.

a = "1 54 0 -245 44 32 -1 -48 123"

high_and_low(a)

input()
