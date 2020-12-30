def dirReduc(arr):
    NS = ["NORTH", "SOUTH"]
    SN = ["SOUTH", "NORTH"]
    EW = ["EAST", "WEST"]
    WE = ["WEST", "EAST"]

    i = -1
    while i < len(arr)-1 :
        i += 1
        if arr[i:i+2] == NS or arr[i:i+2] == SN :
            del arr[i:i+2]
            i=-1
        elif arr[i:i+2] == EW or arr[i:i+2] == WE :
            del arr[i:i+2]
            i = -1
        else : continue
    print(arr)


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
input()
