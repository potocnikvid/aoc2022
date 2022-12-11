f = open('input1.txt', 'r')
lines = f.readlines()
f.close()

sums = []
curr_sum = 0
for line in lines:
    line = line.strip(" ")
    if line == '\n':
        sums.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(line)

sums.sort()
print(sum(sums[-3:]))