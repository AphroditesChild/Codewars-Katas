def longest_slide_down(pyramid):
    slides = [[0 for elem in base] for base in pyramid]
    slides[0][0] = pyramid[0][0]

    for b in range(1, len(pyramid)) :
        for e in range(len(pyramid[b])) :
            if e == 0 :
                slides[b][e] = slides[b-1][0] + pyramid[b][e]
            elif e == len(pyramid[b])-1 :
                slides[b][e] = slides[b-1][-1] + pyramid[b][e]
            elif e > 0 and e < len(pyramid[b])-1 :
                slides[b][e] = max(slides[b-1][e], slides[b-1][e-1]) + pyramid[b][e]

    print(slides)
    print(max(max(x) for x in slides))

longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])

input()
