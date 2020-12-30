def boxes(N):
    BOXES = []
    for i in range(N - int(N**0.5)-1):
        if i < int(N**0.5)-1 or (i+1)%int(N**0.5) != 0:
            BOXES.append( ((i, i+1), (i, i+int(N**0.5)), (i+1, i+1+int(N**0.5)), (i+int(N**0.5), i+int(N**0.5) +1)) )
    return BOXES

print(boxes(9))

def dots_and_boxes(AR):
    ar = [(a,b) if b>a else (b,a) for (a,b) in AR]
    print(ar)
    nDots = max(n for tup in ar for n in tup)+1
    BOXES = boxes(nDots)
    print("Boxes:", BOXES)
    move = 1
    (score1,score2) = (0,0)
    while move <= len(ar):
        print("Moves ["+str(move)+"]:", ar[:move])
        for box in BOXES :
            if set(box).issubset(set(ar[:move+1])):
                print(ar[move-1], "Box", box, "completed!")
                BOXES.remove(box)
                print("Boxes left:", BOXES)
                if move %2==0 :
                    (score1, score2) = (score1, score2+1)
                else :
                    (score1, score2) = (score1+1, score2)

        move += 1
    print("\n\n")
    print("SCORE >>", (score1,score2))

dots_and_boxes( ((0,1),(7,8),(1,2),(6,7),(0,3),(8,5),(3,4),(4,1),(4,5),(2,5),(3,6),(7,4)) )
input()



#  0 1 2
#  3 4 5
#  6 7 8

#9 --> 0 1 3 4   / 16 --> 0 1 2 4 5 6 8 9 10
