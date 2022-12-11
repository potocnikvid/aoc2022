f = open('input1.txt', 'r')
lines = f.readlines()
f.close()

max = 0
curr_max = 0
for line in lines:
    line = line.strip(" ")
    if line == '\n':
        max = max if max > curr_max else curr_max
        curr_max = 0
    else:
        curr_max += int(line)

print(max)
