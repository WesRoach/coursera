# Uses python3
import sys


def get_change(m):
    denominations = [10, 5, 1]
    coins = 0
    for denomination in denominations:
        if m >= denomination:
            coins_of_denomination = m // denomination
            coins += coins_of_denomination
            m -= coins_of_denomination * denomination
    return coins


if __name__ == "__main__":
    m = int(input())
    print(get_change(m))
