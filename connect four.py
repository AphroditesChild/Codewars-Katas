def who_is_winner(pieces_position_list):

    grid = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}

    for k in grid:
        while len(grid[k]) != 6:
            grid[k].append('O')

    for move in pieces_position_list:
        grid[move.split('_')[0]][grid[move.split('_')[0]].index('O')] = move.split('_')[1][0]


        string = "".join([color for k in grid for color in grid[k]])
        print(string)

        for col in grid:
            if "RRRR" in "".join(grid[col]) : return "Red"
            if "YYYY" in "".join(grid[col]) : return "Yellow"

        for i in range(24):
            if string[i]+string[i+6]+string[i+12]+string[i+18]=="RRRR" : return "Red"
            if string[i]+string[i+6]+string[i+12]+string[i+18]=="YYYY" : return "Yellow"

        for i in range(21):
            if i % 6 < 3:
                print(string[i]+string[i+7]+string[i+14]+string[i+21])
                if string[i]+string[i+7]+string[i+14]+string[i+21]=="RRRR" : return "Red"
                if string[i]+string[i+7]+string[i+14]+string[i+21]=="YYYY" : return "Yellow"

        for i in range(24):
            if i % 6 >=u 3:
                print(string[i]+string[i+5]+string[i+10]+string[i+15])
                if string[i]+string[i+5]+string[i+10]+string[i+15]=="RRRR" : return "Red"
                if string[i]+string[i+5]+string[i+10]+string[i+15]=="YYYY" : return "Yellow"
    # Found nothing...
    return "Draw"

print(who_is_winner([
"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]))

input()
