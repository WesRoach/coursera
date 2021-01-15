# %load_ext autoreload
# %autoreload 2

from chinese_remainder_theorem import ExtendedEuclid, ChineseRemainderTheorem

x, y = ExtendedEuclid(17, 11)

ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207)

295310485 * 8217207

579510303168901 % 686579304

# ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207) = 2426627384515395 mod 686579304 != 295310485

ChineseRemainderTheorem()

ExtendedEuclid(11, 17)

# +
#  3 mod 11    7 mod 17
# ra      a   rb      b
# ax + by = 1
# x = -3
# y =  2

# n = 
# ra * b * y + rb * a * x
(3 * 17 * 2 + 7 * 11 * -3) % (11 * 17)
# -


