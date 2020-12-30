def snail(snail_map):
    spiral = []
    while len(snail_map)>1:
        spiral += snail_map.pop(0) + [item.pop(-1) for item in snail_map[0:]] + snail_map.pop(-1)[::-1] + [item.pop(0) for item in snail_map[::-1]]
        print(snail_map)
    return spiral + snail_map[0] if len(snail_map)==1 else spiral




array = [
         [1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]
        ]
print(snail(array))

input()
