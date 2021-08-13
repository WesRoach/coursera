def dollars_in_days(
    starting_dollars: int = 1_000,
    compound: float = 0.10,
    target_dollars: int = 1_000_000,
):
    dollars = starting_dollars
    day = 1
    print(f"Day: {day}; Dollars: {dollars}")
    while dollars < target_dollars:
        dollars += dollars * compound
        day += 1
        print(f"Day: {day}; Dollars: {dollars}")


dollars_in_days()
