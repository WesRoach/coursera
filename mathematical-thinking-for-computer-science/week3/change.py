def change_3_5(amount):
    assert amount >= 8
    if amount == 8:
        return [3, 5]
    if amount == 9:
        return [3, 3, 3]
    if amount == 10:
        return [5, 5]

    coins = change_3_5(amount - 3)
    coins.append(3)

    return coins

# print(change_3_5(16))

def change_5_7(amount):
    if amount == 10:
        return [5, 5]
    if amount == 12:
        return [5, 7]
    if amount == 14:
        return [7, 7]

    if amount % 5 == 0:
        coins = change_5_7(amount - 5)
        coins.append(5)
    else:
        coins = change_5_7(amount - 7)
        coins.append(7)

    return coins

print(change_5_7(19))
print(change_5_7(21))
print(change_5_7(28))
print(change_5_7(49))
