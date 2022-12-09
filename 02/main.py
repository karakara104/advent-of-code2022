# Written by karakara104

# Points
points_play = {'A': 1, 'B':2, 'C':3}
translation = {ord('X'):ord('A'), ord('Y'):ord('B'), ord('Z'):ord('C')}
LOSS = 0
DRAW = 3
WIN = 6

points_win = {'X':LOSS, 'Y':DRAW, 'Z':WIN}

def win(play_opponent, play_me):
    """
    Returns the number of points I won in the Rock Paper Scissors round
    play_opponent : A, B or C (rock, paper, scissor)
    play_me : X, Y, Z (rock, paper, scissor)
    Loss = 0
    Draw = 3
    Win = 6
    Rock = +1
    Paper = +2
    Scissor = +3
    """
    points = 0

    # replayce XYZ by ABC
    play_me = play_me.translate(translation)

    # Get points based on what I played
    points += points_play[play_me]

    # Is there a draw ?
    if play_me == play_opponent: 
        # Draw
        points += DRAW
    elif play_me == 'A' and play_opponent == 'C':
        # I play rock and he plays scissors : I win
        points += WIN
    elif play_me == 'B' and play_opponent == 'A':
        # I play paper and he plays rock : i win
        points += WIN
    elif play_me == 'C' and play_opponent == 'B':
        # I play scissors and he plays paper : I win
        points += WIN 
    return points

def determine_play(play_opponent, win_situation):
    """
    Returns the number of points earned in stage two :
    win_situation : X for loss, Y for draw, Z for win
    play_opponent : A rock, B paper, C scissors
    """
    points = 0
    
    # Get points based on the win situation
    points += points_win[win_situation]

    # What should I play ?
    if win_situation == 'X':
        # Loss
        if play_opponent == 'A':
            points += points_play['C']
        elif play_opponent == 'B':
            points += points_play['A']
        elif play_opponent == 'C':
            points += points_play['B']

    elif win_situation == 'Y':
        # Draw
        points += points_play[play_opponent]
    elif win_situation == 'Z':
        # win
        if play_opponent == 'A':
            points += points_play['B']
        elif play_opponent == 'B':
            points += points_play['C']
        elif play_opponent == 'C':
            points += points_play['A']
    return points


my_points = 0
my_points_2 = 0
# read input
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        my_points += win(*line.split(' '))
        my_points_2 += determine_play(*line.split(' '))

print('My points: ', my_points)
print('My points with the second strategy : ', my_points_2)

