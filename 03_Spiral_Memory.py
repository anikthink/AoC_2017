import math
input = 361527
side = int(math.sqrt(input))
side = side if side % 2 != 0 else side - 1
end = side ** 2
steps = (side - 1)
if end == input:
    print (steps)
else:
    steps = steps + 1
    pos = side
    while end < input:
        end = end + 1
        pos = pos - 1
        if end == input:
            break
        if pos > (side) // 2:
            steps = steps - 1
        else:
            steps = steps + 1
        if pos == 0:
            pos = side + 1
    print (steps, ' ', pos, ' ', side)
