f = open('input.txt', 'r')
lines = f.readlines()
f.close()

score = 0
for pair in lines:
    pair = pair.strip()
    elf1  = pair.split(',')[0]
    elf2  = pair.split(',')[1]
    elf1_start = int(elf1.split('-')[0])
    elf1_end = int(elf1.split('-')[1])
    elf2_start = int(elf2.split('-')[0])
    elf2_end = int(elf2.split('-')[1])

    elf1_range = range(elf1_start, elf1_end + 1)
    elf2_range = range(elf2_start, elf2_end + 1)

    # get the intersection of the two ranges
    intersection = set(elf1_range).intersection(set(elf2_range))
    if intersection:
        score += 1
print(score)
