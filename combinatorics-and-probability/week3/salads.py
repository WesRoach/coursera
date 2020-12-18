from itertools import combinations_with_replacement

salads = []
for c in combinations_with_replacement("TBL", 4):
    salads.append(c)

print(salads)
print(len(salads))

salads = []
for c in combinations_with_replacement("TBLE", 7):
    salads.append(c)

print(salads)
print(len(salads))
