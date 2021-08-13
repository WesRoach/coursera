k = 0
stop = False
while stop is False:
    val = 2 ** k
    str_val = str(val)
    print(f"k: {k}; str_val: {str_val}")
    if str_val[0:2] == "10":
        print(val)
        stop = True
    k += 1
