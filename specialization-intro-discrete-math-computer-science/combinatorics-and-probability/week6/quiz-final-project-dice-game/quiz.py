def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    # write your code here
    for val1 in dice1:
        for val2 in dice2:
            if val1 > val2:
                dice1_wins += 1
            if val2 > val1:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    # write your code here
    # use your implementation of count_wins method if necessary
    wins_by_index = [0 for x in range(0, len(dices))]
    # if a dice wins len(dices) - 1 games, then it meets the criteria
    wins_to_win = len(dices) - 1

    # Create combinations of dice with index of each dice from `dices`
    # [((0, [1,2,3,4,5,6]), (1, [1,2,3,4,5,6])), (next-combination), (etc)]
    combinations = []
    for i in range(0, len(dices) - 1):
        for j in range(i + 1, len(dices)):
            combinations.append(((i, dices[i]), (j, dices[j])))

    combination_wins = dict()

    # Decide which die would win more often between pairing, and increment wins
    # for this die by index of the die in `wins_by_index`
    for combination in combinations:
        wins = count_wins(combination[0][1], combination[1][1])
        combination_key = (combination[0][0], combination[1][0])
        combination_wins[combination_key] = wins
        if wins[0] > wins[1]:
            wins_by_index[combination[0][0]] += 1
        if wins[1] > wins[0]:
            wins_by_index[combination[1][0]] += 1

    for idx, val in enumerate(wins_by_index):
        if val == wins_to_win:
            return idx

    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()

    # if there is a single best die - pick first, pick that die
    best_dice = find_the_best_dice(dices)
    if best_dice != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = best_dice
        return strategy

    # If not a single best die - figure out which die beats what
    strategy["choose_first"] = False
    for i in range(len(dices)):
        strategy[i] = (-1, 0)

    # Create combinations of dice with index of each dice from `dices`
    # [((0, [1,2,3,4,5,6]), (1, [1,2,3,4,5,6])), (next-combination), (etc)]
    combinations = []
    for i in range(0, len(dices) - 1):
        for j in range(i + 1, len(dices)):
            combinations.append(((i, dices[i]), (j, dices[j])))

    # Decide which die would win more often between pairing
    for combination in combinations:
        wins = count_wins(combination[0][1], combination[1][1])
        d1_idx = combination[0][0]
        d1_wins = wins[0]
        d2_idx = combination[1][0]
        d2_wins = wins[1]
        # {i: (lost_to, how_much)}
        win_difference = abs(d1_wins - d2_wins)
        if d1_wins > d2_wins:
            if strategy[d2_idx][1] < win_difference:
                strategy[d2_idx] = (d1_idx, win_difference)
        if d2_wins > d1_wins:
            if strategy[d1_idx][1] < win_difference:
                strategy[d1_idx] = (d2_idx, win_difference)

    # convert strat tuples into index of die to be picked after first die pick
    for i in range(len(dices)):
        strategy[i] = strategy[i][0]

    return strategy
