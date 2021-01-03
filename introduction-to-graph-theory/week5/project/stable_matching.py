def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he_idx = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he_idx]
        # Find a woman to propose to
        she_idx = hisPreferences[nextManChoice[he_idx]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she_idx]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she_idx]

        # Write your code here

        # Now "he" proposes to "she".
        # Decide whether "she" accepts, and update the following fields
        accept = currentHusband is None or herPreferences.index(
            currentHusband
        ) > herPreferences.index(he_idx)

        if accept is True:
            # 1. manSpouse
            manSpouse[he_idx] = she_idx
            if currentHusband is not None:
                manSpouse[currentHusband] = None
            # 2. womanSpouse
            womanSpouse[she_idx] = he_idx
            # 3. unmarriedMen
            unmarriedMen.remove(he_idx)
            if currentHusband is not None:
                unmarriedMen.append(currentHusband)

        # 4. nextManChoice
        nextManChoice[he_idx] += 1

    # Note that if you don't update the unmarriedMen list,
    # then this algorithm will run forever.
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse
