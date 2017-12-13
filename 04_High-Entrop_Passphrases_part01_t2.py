with open('04_Input.txt') as f:
    a = f.readlines()
    correct = 0
    correct_2 = 0
    for line in a:
        b = line.split()
        c = set(b)
        e = ""
        d = set(["".join(sorted(word)) for word in b])
        if len(b) == len(c):
            correct += 1
        if len(b) == len(d):
            correct_2 += 1
    print (correct)
    print (correct_2)
