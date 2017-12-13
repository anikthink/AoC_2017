with open('05_Input.txt') as f:
    a = f.readlines()
    a = list(map(int, a))
    i = 0
    steps = 0
    while i >= 0 and i < len(a):
        jump = a[i]
        if a[i] > 2:
            a[i] -= 1
        else:
            a[i] += 1
        steps += 1
        i += jump
    print (steps)
