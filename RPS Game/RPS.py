import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
        else:
            results["p2"] += 1

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return win_rate

def quincy_strategy(opponent_history):
    if opponent_history[-4]=='R' and opponent_history[-3]=='P' and opponent_history[-2]=='P' and opponent_history[-1]=='S':
        return 'P'
    elif opponent_history[-4]=='P' and opponent_history[-3]=='P' and opponent_history[-2]=='S' and opponent_history[-1]=='R':
        return 'P'
    elif opponent_history[-4]=='P' and opponent_history[-3]=='S' and opponent_history[-2]=='R' and opponent_history[-1]=='R':
        return 'S'
    elif opponent_history[-4]=='S' and opponent_history[-3]=='R' and opponent_history[-2]=='R' and opponent_history[-1]=='P':
        return 'S'
    elif opponent_history[-4]=='R' and opponent_history[-3]=='R' and opponent_history[-2]=='P' and opponent_history[-1]=='P':
        return 'R'

def kris_strategy(opponent_history):
    if len(opponent_history)%3==0:
        return 'P'
    if len(opponent_history)%3==1:
        return 'R'
    if len(opponent_history)%3==2:
        return 'S'

def abbey_strategy(prev_play,opponent_history):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    if opponent_history[-2]==opponent_history[-1]:
        if prev_play=='P':
            return ideal_response[prev_play]
        elif prev_play=='R':
            return ideal_response[prev_play]
        elif prev_play=='S':
            return ideal_response[prev_play]
    elif opponent_history[-2]!=opponent_history[-1]:
        if opponent_history[-3]!=opponent_history[-2]:
            if prev_play=='P':
                return ideal_response[prev_play]
            elif prev_play=='R':
                return ideal_response[prev_play]
            else:
                return ideal_response['S']
        else:
            return prev_play

def player(prev_play, opponent_history=[]):
    guess = ''

    if not prev_play:
        opponent_history.clear()

    if len(opponent_history) <= 5:
        guess = 'P'

    elif opponent_history[1] == 'P' and opponent_history[2] == 'S' and opponent_history[3] == 'S':
        guess = kris_strategy(opponent_history)

    elif opponent_history[1] == 'P' and opponent_history[2] == 'P' and opponent_history[3] == 'S':
        guess = abbey_strategy(prev_play, opponent_history)

    elif opponent_history[1] == 'R' and opponent_history[2] == 'R' and opponent_history[3] == 'S':
        guess = abbey_strategy(prev_play, opponent_history)

    elif opponent_history[1] == 'R' and opponent_history[2] == 'P' and opponent_history[3] == 'P':
        guess = quincy_strategy(opponent_history)

    opponent_history.append(prev_play)
    return guess
