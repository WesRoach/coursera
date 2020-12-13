def is_divisible(val, div):
    if val % div == 0:
        return True


def cnt_divisible_by(val: int = 1000):
    cnt = 0
    for i in range(1, val + 1):
        if is_divisible(i, 2):
            cnt += 1
        elif is_divisible(i, 3):
            cnt += 1

    return cnt


def cnt_not_divisible_by(val: int = 1000):
    cnt = 0
    for i in range(1, val + 1):
        if not is_divisible(i, 2) and not is_divisible(i, 3):
            cnt += 1

    return cnt


print(cnt_divisible_by())
print(cnt_not_divisible_by())
