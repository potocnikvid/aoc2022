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

    if (elf1_start >= elf2_start and elf1_end <= elf2_end) or (elf2_start >= elf1_start and elf2_end <= elf1_end):
        score += 1

print(score)
