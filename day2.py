from functools import reduce

def rps(file):
    lines = f.readlines()
    points = 0

    def player_move(myMove):
        match myMove:
            case 'X':
                return points + 1
            case 'Y':
                return points + 2
            case 'Z':
                return points + 3


    for i in lines:
        opponent_move = i[0]
        my_move = i[2]

        if my_move == 'X' and opponent_move == 'C' or my_move == 'Y' and opponent_move == 'A' or my_move == 'Z' and opponent_move == 'B':
            points = player_move(my_move) + 6
        elif my_move == 'X' and opponent_move == 'B' or my_move == 'Y' and opponent_move == 'C' or my_move == 'Z' and opponent_move == 'A':
            points = player_move(my_move)
        else:
            points = player_move(my_move) + 3

    print(f'Final score = {points}')

def rps2(file):
    lines = f.readlines()
    points = 0

    def player_move(myMove):
        # A = 2 B = 3 C = 1
        match myMove:
            case 'X': 
                if opponent_move == 'A': 
                    return points + 3
                elif opponent_move == 'B':
                    return points + 1
                else:
                    return points + 2
            
            case 'Y':
                if opponent_move == 'A':
                    return points + 4
                elif opponent_move == 'B':
                    return points + 5
                else:
                    return points + 6

            case 'Z':
                if opponent_move == 'A':
                    return points + 8
                elif opponent_move == 'B':
                    return points + 9
                else:
                    return points + 7


    for i in lines:
        opponent_move = i[0]
        my_move = i[2]

        points = player_move(my_move)

    print(f'Final score part 2 = {points}')

with open('input.txt') as f:
    # rps(f)
    rps2(f)
    