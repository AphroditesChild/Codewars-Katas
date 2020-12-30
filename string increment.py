import re

def increment_string(strng):
    num = re.findall("[0-9]+$", strng)
    if num != []:
        num = num[0]
    else :
        return strng+"1"
    print(num)

    digit19 = re.findall("[1-9]+[0-9]*", num)
    if digit19 != []:
        digit19 = digit19[0]
    else :
        digit19 = ""

    zeros = re.findall("^[0]+", num)
    if zeros != []:
        zeros = zeros[0]
    else:
        zeros = ""
    print(zeros)
    print(digit19)


    if digit19 != "":
        incDigits = str(int(digit19)+1)
        if len(incDigits) > len(digit19):
            if zeros != "":
                NUM = zeros[:-1]+incDigits
            else :
                NUM = incDigits
        else :
            NUM = zeros+incDigits
    else :
            NUM = zeros[:-1]+"1"

    return strng[:len(strng)-len(num)]+NUM



print(increment_string("fogh00obar0999"))

input()
quit()
