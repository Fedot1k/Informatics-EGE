for x in range(111):
    f1 = x * 111**3 + 3 * 111**2 + 2 * 111 + 1
    f2 = 1 * 211**3 + 7 * 211**2 + x * 211 + 4
    f = f1 + f2
    if f%111==0:
        print(f/111)