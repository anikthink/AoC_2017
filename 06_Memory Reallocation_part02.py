with open('06_Input.txt') as f:
    b = list(map(int, f.read().strip().split()))
    a = []      #To store seen states
    check = True
    steps = 0
    x = 0
    while check == True:
        steps += 1
        high = max(b)
        iH = b.index(high)
        b[iH] = 0
        for i in range (high):
            iH += 1
            b[iH % len(b)] += 1
        if b in a:
            if x == 0:
                a.clear()
                steps = 0
                x += 1
            else:
                check = False
        a.append(b[:])
    print (b)
    print (steps)
